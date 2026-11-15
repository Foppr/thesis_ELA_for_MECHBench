import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested trigonometric chaos with fractal-like recursion
        f1 = 0.5 * np.sum(np.sin(3.0 * np.pi * x) * np.cos(7.0 * np.pi * x) * 
                          np.sin(11.0 * np.pi * x) * np.cos(13.0 * np.pi * x))
        
        # Adaptive polynomial coupling with dynamic exponents and cross-terms
        f2 = 0.4 * np.sum((x**4 + 0.2 * x**5 + 0.03 * x**6) * 
                          np.abs(x)**0.8 * np.sin(0.5 * np.sum(x)))
        
        # Stochastic resonance modulation with multi-scale noise interaction
        noise = np.sin(0.2 * np.sum(x**3)) * np.cos(0.1 * np.sum(x**2)) * 
                np.exp(-0.03 * np.sum(np.abs(x)**1.5))
        f3 = 0.3 * np.sum(np.exp(-0.15 * np.abs(x)) * np.sin(15.0 * x) * 
                          np.cos(10.0 * x) * noise)
        
        # Multi-scale fractal interaction with log-scaled and power-modulated components
        f4 = 0.25 * np.sum(np.sin(np.log(np.abs(x) + 2.0)) * 
                           np.cos(np.log(np.abs(x) + 2.0)) * 
                           np.exp(-0.2 * np.abs(x)))
        
        # Saddle point distribution with hyperbolic and polynomial components with variable coefficients
        f5 = 0.28 * np.sum(np.tanh(x) * (x**3 - x) * np.cos(5.0 * x) * 
                           np.sin(0.3 * np.sum(x)))
        
        # Enhanced recursive fractal structure with polynomial and trigonometric coupling
        f6 = 0.18 * np.sum((x**3 + 0.2 * x**4) * np.sin(6.0 * x) * 
                           np.cos(5.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Cross-term coupling with exponential decay, sinusoidal perturbations, and adaptive scaling
        f7 = 0.22 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(11.0 * x) * 
                           np.cos(9.0 * x) * np.sin(0.2 * np.sum(x**2)))
        
        # Additional complex interaction term with nested logarithmic and exponential components
        f8 = 0.15 * np.sum(np.sin(0.7 * x) * np.cos(0.4 * x) * 
                           np.exp(-0.15 * x**2) * np.log(np.abs(x) + 1.2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8