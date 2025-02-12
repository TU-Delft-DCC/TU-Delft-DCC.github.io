```matlab
function result = runTestSuite(varargin)
%RUNTESTSUITE - Run all tests and produce coverage report
%
% Requires Matlab version >= R2017a
%
% This script is designed to be placed with the folder tests/ following
% the folder organization as seen below:
%
% - root/
%   | - src/
%   |   | - function_1.m
%   |   \ - function_2.m
%   |
%   \ - tests/
%       | - reports/    % Folder will be generated during testing
%       | - runTestSuite.m
%       | - testFunction_1.m
%       \ - testFunction_2.m
% 
% Resources:
% https://nl.mathworks.com/help/matlab/ref/matlab.unittest.plugins.codecoverageplugin-class.html
%
% 
% Parameters
% ----------
% srcFolderName : char, optional
%   Name of the source code directory. Defaults to 'src'.
% TestTag : char, optional
%   Only tests with this tag will be run. Defaults to running all tests,
% ExcludedFiles : cell, optional
%   List of filenames that will be excluded from the coverage report.
%   Defaults to reading the file 'excludedFiles.json'.
% PDFReport : logical, optional
%   Add to generate a PDF report. Defaults to true.
% JUnitResults : logical, optional
%   Add to generate a JUnit report. Defaults to true.
% CoberturaCodeCoverageXML : logical, optional
%   Add to generate a XML Cobertura coverage report. Defaults to true.
% CoberturaCodeCoverageHTML : logical, optional
%   Add to generate a HTML Cobertura coverage report. Defaults to true.
%
%
% Returns
% -------
% result : matlab.unittest.TestResult
%
%
% Examples
% --------
%       result = run_testsuite('TestTag', 'Unit');   
%       result = run_testsuite('TestTag', 'Unit', ...
%                'ExcludedFiles', 'function_1.m');
% 

p = inputParser;
p.addParameter('srcFolderName', 'src', @ischar);
p.addParameter('TestTag', '', @ischar);
p.addParameter('ExcludedFiles', {}, @iscell);
p.addParameter('PDFReport', true, @islogical);
p.addParameter('JUnitResults', true, @islogical);
p.addParameter('CoberturaCodeCoverageXML', true, @islogical);
p.addParameter('CoberturaCodeCoverageHTML', true, @islogical);

p.parse(varargin{:});

srcFolderName            = p.Results.srcFolderName;
testTag                  = p.Results.TestTag;
producePDFReport         = p.Results.PDFReport;
produceJUnit             = p.Results.JUnitResults;
produceCoberturaXML      = p.Results.CoberturaCodeCoverageXML;
produceCoberturaHTML     = p.Results.CoberturaCodeCoverageHTML;
excludedFiles            = p.Results.ExcludedFiles;

% Import required Matlab libraries
import matlab.unittest.TestSuite
import matlab.unittest.TestRunner
import matlab.unittest.plugins.XMLPlugin
import matlab.unittest.plugins.TestReportPlugin
import matlab.unittest.plugins.CodeCoveragePlugin
import matlab.unittest.plugins.codecoverage.CoverageReport
import matlab.unittest.plugins.codecoverage.CoberturaFormat
import matlab.unittest.selectors.HasTag

% Define folder structure
rootDir = getRootDir();
testFolder = fullfile(rootDir, 'tests');
srcFolder = fullfile(rootDir, srcFolderName);
reportFolder = fullfile(testFolder, 'reports');

% Add source folder plus all subfolders to the path.
addFilesToPath(srcFolder);

% Create test suite
suite = TestSuite.fromFolder(testFolder, 'IncludingSubfolders', true);
runner = TestRunner.withTextOutput;

% Exclude files from coverage report
codeFilePaths = excludeFilesFromCoverage(srcFolder, excludedFiles);

% Produce JUnit report
if produceJUnit
    mkdirIfNeeded(reportFolder)
    xmlFile = fullfile(reportFolder, 'junit.xml');
    runner.addPlugin(XMLPlugin.producingJUnitFormat(xmlFile));
end

% Prepare HTML format output
if produceCoberturaHTML
    mkdirIfNeeded(reportFolder)
    reportFileHTML = 'coverage.html';
    pluginHTML = CodeCoveragePlugin.forFile(codeFilePaths,...
    'Producing', CoverageReport(reportFolder, 'MainFile', reportFileHTML));
    runner.addPlugin(pluginHTML);
end

% Prepare XML format output
if produceCoberturaXML
    mkdirIfNeeded(reportFolder)
    reportFileXML = fullfile(reportFolder, 'coverage.xml');
    reportFormat = CoberturaFormat(reportFileXML);
    pluginXML = CodeCoveragePlugin.forFile(codeFilePaths,...
        'Producing', reportFormat);
    runner.addPlugin(pluginXML);
end

% Produce PDF test report (Not supported on MacOS platform)
if producePDFReport
    if ismac
        warning('MATLAB:testArtifact:unSupportedPlatform', ...
            'Producing a PDF test report is not currently supported on MacOS platforms.');
    else
        mkdirIfNeeded(reportFolder);
        reportFilePDF = fullfile(reportFolder, 'testreport.pdf');
        runner.addPlugin(TestReportPlugin.producingPDF(reportFilePDF));        
    end
end

% Select tests with specific TestTag
if testTag
    if ~isempty(suite.selectIf(HasTag(testTag)))
        suite = suite.selectIf(HasTag(testTag));
    end
end

% Run testsuite
result = runner.run(suite);

% Print coverage result to command window
if isfile(reportFileXML)
    printCoverage(reportFileXML)
end


function rootDir = getRootDir
    here = pwd;
    idx = strfind(here, filesep);
    rootDir = fullfile(here(1:idx(end)-1));

function mkdirIfNeeded(dir)
    if exist(dir,'dir') ~= 7
        mkdir(dir);
    end

function excludedFiles = readExcludedFiles
    try
        json = fileread('excludedFiles.json');
        excludedFiles = jsondecode(json);
    catch ME
        msg = strcat(ME.message, ' No files will be excluded from code coverage.');
        warning(msg)
    end

function codeFilePaths = excludeFilesFromCoverage(srcFolder, excludedFiles)
    dirOut = dir(fullfile(srcFolder, '**', '*.m'));
    codeFilePaths = string({dirOut.folder}) + filesep + string({dirOut.name});
    codeFilePaths(contains(codeFilePaths, excludedFiles)) = [];

function addFilesToPath(srcFolder)
    if exist(srcFolder, 'dir') == 7
        addpath(genpath(srcFolder));
    else
        error('Cannot find source folder: %s', srcFolder);
    end

function printCoverage(coverageFile)
    S = parseXML(coverageFile);
    index = find(strcmp('line-rate', {S.Attributes.Name}));
    coverage = str2double(S.Attributes(index).Value)*100;
    formatSpec = '%.2f%% covered \n';
    fprintf(formatSpec, coverage)

```