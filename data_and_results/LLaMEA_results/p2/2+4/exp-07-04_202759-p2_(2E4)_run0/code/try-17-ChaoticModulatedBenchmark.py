import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component for global shaping with higher degree
        poly = np.sum(x**6)
        
        # Trigonometric component for local modulation with varying frequencies
        trig = np.sum(np.sin(0.7 * x) * np.cos(0.4 * x) * np.sin(0.2 * x))
        
        # Radial basis component for center attraction with adaptive width
        rb = np.sum(np.exp(-0.05 * (x**2)) * np.cos(0.1 * x))
        
        # Enhanced cross-term interaction to create stronger non-separability
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j])) + 
                         np.cos(x[i] * x[j]) * np.sin(0.2 * (x[i] - x[j])))
        
        # Improved chaotic modulation with logistic-like behavior and multiple scales
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.exp(-0.03 * np.abs(x[i])) * 
                       np.sin(7 * np.pi * x[i]) * 
                       np.cos(3 * np.pi * x[i]))
        
        # Additional harmonic component to increase function complexity
        harmonic = np.sum(np.sin(0.5 * x) * np.cos(0.3 * x) * np.sin(0.1 * x) * np.cos(0.05 * x))
        
        # Combine all components with optimized weights
        return (0.5 * poly + 
                0.25 * trig + 
                0.15 * rb + 
                0.1 * cross + 
                0.12 * chaotic + 
                0.08 * harmonic + 
                0.05 * np.sum(x**8))