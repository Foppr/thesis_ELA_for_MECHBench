import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with variable exponents and adaptive scaling
        poly = np.sum(np.power(np.abs(x), 3.2) * np.sin(0.5 * x) ** 2)
        
        # Multi-scale trigonometric component with phase coupling and frequency mixing
        trig = np.sum(np.sin(1.2 * x) * np.cos(0.8 * x) * np.sin(0.4 * x) * np.cos(0.2 * x) * np.sin(0.1 * x))
        
        # Radial basis with enhanced localization and multi-center attraction
        rb = np.sum(np.exp(-0.05 * (x**2)) * np.cos(0.2 * x) * np.sin(0.1 * x) * np.cos(0.05 * x))
        
        # Cross-term interactions with non-linear coupling and dynamic coupling strength
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (np.sin(x[i] * x[j] * 0.5) * np.cos(0.3 * (x[i] + x[j])) + 
                         np.cos(x[i] * x[j] * 0.7) * np.sin(0.2 * (x[i] - x[j])) + 
                         np.sin(0.4 * x[i]) * np.cos(0.6 * x[j]) * np.sin(0.3 * x[i] * x[j]))
        
        # Chaotic modulation with multiple logistic maps and dynamic frequency mixing
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.exp(-0.06 * np.abs(x[i])) * 
                       np.sin(7 * np.pi * x[i]) * 
                       np.cos(5 * np.pi * x[i]) * 
                       np.sin(3 * np.pi * x[i]) * 
                       np.cos(2 * np.pi * x[i]))
        
        # Harmonic and fractional component with increased complexity
        harmonic = np.sum(np.sin(0.7 * x) * np.cos(0.5 * x) * np.sin(0.3 * x) * np.cos(0.15 * x) * np.sin(0.08 * x) * np.cos(0.04 * x))
        
        # Fractional polynomial term with variable exponent for additional non-linearity
        frac_poly = np.sum(np.power(np.abs(x), 1.9))
        
        # Additional high-frequency oscillation component
        high_freq = np.sum(np.sin(10 * x) * np.cos(8 * x) * np.sin(6 * x) * np.cos(4 * x))
        
        # Combine all components with optimized weights for better conditioning and performance
        return (0.35 * poly + 
                0.2 * trig + 
                0.15 * rb + 
                0.18 * cross + 
                0.12 * chaotic + 
                0.08 * harmonic + 
                0.06 * frac_poly + 
                0.05 * high_freq + 
                0.05 * np.sum(x**12))