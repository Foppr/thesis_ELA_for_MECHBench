import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component for chaos
        logistic = np.sum(4.0 * np.abs(x) * (1.0 - np.abs(x)))
        
        # Trigonometric wave interference with varying frequencies
        trig = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * 
                      np.sin(5.0 * np.pi * x) * np.cos(7.0 * np.pi * x))
        
        # Power-law interactions with fractal scaling
        power = np.sum(np.abs(x)**(1.5 + 0.5 * np.sin(x)) + 
                       0.3 * np.abs(x)**(2.0 + 0.3 * np.cos(x)))
        
        # Nested saddle points and local minima via nested functions
        nested = np.sum(np.sin(np.pi * x) * np.exp(-0.1 * np.abs(x)) * 
                        np.cos(np.pi * np.log(np.abs(x) + 1e-8)))
        
        # Add a small random perturbation to increase ruggedness
        rand_perturb = 0.01 * np.sum(np.sin(100.0 * x) * np.cos(150.0 * x))
        
        return logistic + trig + power + nested + rand_perturb