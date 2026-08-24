import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillations with multiple sine and cosine components and fractal-like self-similarity
        chaotic_term = np.sum(np.sin(15 * np.pi * x) * np.cos(12 * np.pi * x) * 
                             np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x) * 
                             np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x) * 
                             np.sin(2 * np.pi * x))
        
        # Stronger polynomial coupling with higher-degree terms and mixed nonlinearities including fractional powers
        poly_term = np.sum(0.8 * x**13 - 9 * x**11 + 15 * x**9 - 12 * x**7 + 8 * x**5 - 4 * x**3 + 2 * x**2 - 1.2 * x)
        
        # Cross-dimensional nonlinear coupling with dynamic phase shifts, interaction weights, and memory-dependent terms
        coupling_term = np.sum((x[:-1] - x[1:])**7 * np.sin(12 * np.pi * x[:-1]) * np.cos(9 * np.pi * x[1:]) + 
                              (x[:-1] + x[1:])**5 * np.cos(11 * np.pi * x[:-1]) * np.sin(7 * np.pi * x[1:]) + 
                              (x[:-1] * x[1:])**3 * np.sin(5 * np.pi * x[:-1]) * np.cos(3 * np.pi * x[1:]))
        
        # Additional high-frequency chaotic correlation terms with varying amplitudes and phase modulations
        corr_term = np.sum(np.sin(18 * np.pi * x) * np.cos(16 * np.pi * x) * 
                          np.sin(14 * np.pi * x) * np.cos(12 * np.pi * x) * 
                          np.sin(10 * np.pi * x) * np.cos(8 * np.pi * x) * 
                          np.sin(6 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Exponential decay with multi-scale oscillations, amplitude modulation, and memory effects
        exp_term = np.sum(np.exp(-0.7 * x**2) * np.sin(12 * np.pi * x) * np.cos(10 * np.pi * x) * 
                         np.sin(8 * np.pi * x) * np.cos(6 * np.pi * x) * np.sin(4 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Memory-dependent interaction term with delayed feedback and cumulative effects
        memory_term = np.sum(np.sin(3 * np.pi * (x[:-1] + 0.5 * x[1:])) * np.cos(2 * np.pi * (x[1:] + 0.3 * x[:-1])) * 
                            np.sin(1.5 * np.pi * (x[:-1] - 0.2 * x[1:])) * np.cos(1.2 * np.pi * (x[1:] - 0.4 * x[:-1])))
        
        # Combine all terms with optimized weights and add a global offset
        return 0.35 * chaotic_term + 0.07 * poly_term + 0.12 * coupling_term + 0.09 * corr_term + 0.18 * exp_term + 0.1 * memory_term + 2.5