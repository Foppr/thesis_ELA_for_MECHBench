import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with higher degree and adaptive scaling
        poly = np.sum(x**8)
        
        # Trigonometric component with multi-scale frequencies and phase modulation
        trig = np.sum(np.sin(0.8 * x) * np.cos(0.5 * x) * np.sin(0.3 * x) * np.cos(0.1 * x))
        
        # Radial basis component with variable width and multi-center attraction
        rb = np.sum(np.exp(-0.03 * (x**2)) * np.cos(0.15 * x) * np.sin(0.05 * x))
        
        # Enhanced cross-term interaction with non-linear coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i] + x[j])) + 
                         np.cos(x[i] * x[j]) * np.sin(0.25 * (x[i] - x[j])) + 
                         np.sin(0.3 * x[i]) * np.cos(0.3 * x[j]))
        
        # Improved chaotic modulation with multiple logistic maps and frequency mixing
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.exp(-0.04 * np.abs(x[i])) * 
                       np.sin(6 * np.pi * x[i]) * 
                       np.cos(4 * np.pi * x[i]) * 
                       np.sin(2 * np.pi * x[i]))
        
        # Additional harmonic and fractional component to increase complexity
        harmonic = np.sum(np.sin(0.6 * x) * np.cos(0.4 * x) * np.sin(0.2 * x) * np.cos(0.1 * x) * np.sin(0.05 * x))
        
        # Fractional polynomial term for additional non-linearity
        frac_poly = np.sum(np.power(np.abs(x), 1.7))
        
        # Combine all components with optimized weights for better conditioning
        return (0.4 * poly + 
                0.2 * trig + 
                0.12 * rb + 
                0.15 * cross + 
                0.13 * chaotic + 
                0.08 * harmonic + 
                0.07 * frac_poly + 
                0.05 * np.sum(x**10))