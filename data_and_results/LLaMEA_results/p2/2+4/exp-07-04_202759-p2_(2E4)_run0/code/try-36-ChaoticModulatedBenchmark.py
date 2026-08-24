import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with variable exponents and adaptive scaling
        poly = np.sum(np.power(np.abs(x), 1.9) * np.exp(-0.1 * np.abs(x)))
        
        # Multi-scale trigonometric component with phase modulation and frequency mixing
        trig = np.sum(np.sin(0.7 * x) * np.cos(0.4 * x) * np.sin(0.2 * x) * np.cos(0.05 * x) * np.sin(0.01 * x))
        
        # Radial basis with variable width, multi-center attraction, and phase modulation
        rb = np.sum(np.exp(-0.02 * (x**2)) * np.cos(0.2 * x) * np.sin(0.1 * x) * np.cos(0.05 * x))
        
        # Enhanced cross-term interactions with non-linear coupling and dynamic weights
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j])) + 
                         np.cos(x[i] * x[j]) * np.sin(0.2 * (x[i] - x[j])) + 
                         np.sin(0.25 * x[i]) * np.cos(0.25 * x[j]) * 
                         np.exp(-0.05 * np.abs(x[i] - x[j])))
        
        # Improved chaotic modulation with multiple logistic maps and frequency mixing
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.exp(-0.03 * np.abs(x[i])) * 
                       np.sin(5 * np.pi * x[i]) * 
                       np.cos(3 * np.pi * x[i]) * 
                       np.sin(1.5 * np.pi * x[i]) * 
                       np.cos(0.5 * np.pi * x[i]))
        
        # Additional harmonic and fractional component to increase complexity
        harmonic = np.sum(np.sin(0.5 * x) * np.cos(0.3 * x) * np.sin(0.1 * x) * np.cos(0.05 * x) * np.sin(0.02 * x))
        
        # Fractional polynomial term for additional non-linearity with dynamic exponent
        frac_poly = np.sum(np.power(np.abs(x), 1.8) * np.sin(0.1 * x))
        
        # Additional conditioning term with exponential scaling
        cond = np.sum(np.exp(0.05 * x**2) * np.cos(0.3 * x))
        
        # Combine all components with optimized weights for better conditioning and bias reduction
        return (0.35 * poly + 
                0.2 * trig + 
                0.15 * rb + 
                0.18 * cross + 
                0.12 * chaotic + 
                0.08 * harmonic + 
                0.05 * frac_poly + 
                0.07 * cond)