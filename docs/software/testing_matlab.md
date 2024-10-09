---
title: Testing with MATLAB
categories:
    - testing
    - matlab
description: "Writing and running tests with MATLAB."
hide-description: true
author_1:
    - name: "DCC Team"
---

In this guide, we will discuss writing and running tests with MATLAB. See the [documentation from Matlab](https://nl.mathworks.com/help/matlab/matlab-unit-test-framework.html) for more information.

## Writing tests

Tests should be kept separate from the code base, usually in a folder `tests/`. The naming convention for writing a test for a particular MATLAB script is to prefix “test_” to the name of the script that is being tested. For example, a test for the file `draw_random_number.m` should be called `test_draw_random_number.m`. In general, Matlab will recognize any scripts that are prefixed or suffixed with the string “test” as tests.

You can find an example below with the matlab syntax for writing [Class-based unit tests](https://nl.mathworks.com/help/matlab/class-based-unit-tests.html):

:::{.callout-note collapse="true" title="Click to view"}
```matlab
% Test classes are created by inheriting (< symbol) the  Matlab Testing 
% framework.
%
% e.g. classdef nameOfTest < matlab.unittest.TestCase
%      end

classdef (TestTags = {'Unit'}) test_example < matlab.unittest.TestCase 
%                              It's convention to name the test file 
%                              test_"filename being tested".m
%
%         TestTags are an optional feature that are useful for identifying 
%         what kind of test you're coding, as you might only want to run 
%         certain tests that are related.

    properties 
        % Class properties are not required, but are useful to contain 
        % common parameters between tests.
    end
    
    methods (TestClassSetup) 
        % TestClassSetup methods are not required, but are usually used to
        % setup common testing variables, or loading data. These methods
        % are executed *prior to* the (Test) methods.
    end
    
    methods (TestClassTeardown) 
        % TestClassTeardown methods are not required, but are useful to
        % delete any files created during the test execution. These methods
        % are executed *after* the (Test) methods.
    end
    
    methods (Test) % Each test is it's own method function, and takes 
                   % testCase as their only argument.

        function test_sumNumbers_returns_expected_value_for_integer_case(testCase) 
        % Use very descriptive test method names - this helps for debugging
        % when error occurs.
                        
            % Call the function you'd like to test, e.g:
%             actualValue = sumNumbers(2,2); % Test example integer case, 2+2
            % Since the function sumNumbers is not defined, the test will
            % fail. Instead, we will define the actual value.
            actualValue = 4;


            expectedValue = 4; % We know that we expect that 2+2 = 4

            testCase.assertEqual(expectedValue, actualValue)
            % Assert functions are the core of unit tests; if it fails,
            % test log will return failed tests and details.
            %
            % They are called as methods of the testCase object.
            %
            % Example assert methods:
            %
            % assertEqual(expected, actual): Passes if the two input values
            %                                are equal.
            % assertTrue(boolValue): Passes if the value or statement is 
            %                        true (e.g. 2>1)
            % assertFalse(boolValue): Passes if the value or statement is
            %                         false (e.g. 1==0)
            %
            % See Matlab's documentation for more assert methods: 
            % https://www.mathworks.com/help/matlab/ref/matlab.unittest.qualifications.assertable-class.html
        end
    end

end
```
:::


## Executing tests
We will create a Matlab script called `run_testsuite.m` in the folder `tests/`. This function can run the tests present in the folder `tests/` and can create test reports.

:::{.callout-note collapse="true" title="Click to view"}
```matlab
function result = run_testsuite(varargin)
%RUNTESTS - Run all tests and produce coverage report
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
%       | - run_testsuite.m
%       | - test_function_1.m
%       \ - test_function_2.m
% 
% Resources:
% https://nl.mathworks.com/help/matlab/ref/matlab.unittest.plugins.codecoverageplugin-class.html
%
% 
% Parameters
% ----------
% srcFolderName : char, optional
%   Name of the source code directory. Defaults to 'pvmd'.
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
%                'ExcludedFiles', {'function_1.m');
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
:::


Additionally, we can selectively run test by defining TestTags. In the example above, we added the tag 'Unit'. You can then call the function in the MATLAB command window to run all tests with the tag 'Unit' with

```matlab
result = run_testsuite('TestTag', 'Unit')
```
:::{.callout-tip}
If you want to quickly check whether your tests pass without having to start up Matlab, you can also call `run_testsuite` from the terminal. In the folder containing the function, execute

```bash
matlab -batch "run_testsuite('TestTag', 'Unit')"
```

:::