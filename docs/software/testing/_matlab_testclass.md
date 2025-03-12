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