import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like high-frequency oscillations with varying amplitudes
        fractal_term = np.sum(np.sin(30 * x_scaled) * np.cos(25 * x_scaled) * 
                             np.sin(15 * x_scaled) * np.cos(10 * x_scaled))
        
        # Quantum interference pattern with phase modulation
        quantum_term = np.sum(np.sin(12 * np.pi * x_scaled + np.sin(8 * np.pi * x_scaled)) * 
                             np.cos(6 * np.pi * x_scaled + np.cos(4 * np.pi * x_scaled)))
        
        # Dynamic penalty landscape with multiple local minima
        penalty_term = np.sum(1.0 / (1.0 + np.exp(-10 * (x_scaled**2 - 0.25))) * 
                             np.sin(20 * np.pi * x_scaled)**2)
        
        # Multi-scale radial symmetry with dynamic scaling factors
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.05) * 
                            np.sin(7 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) * 
                            np.exp(-0.5 * x_scaled**2))
        
        # Coupled exponential and trigonometric terms with adaptive coupling
        coupled_term = np.sum(np.exp(-2 * x_scaled**2) * 
                             (np.sin(18 * np.pi * x_scaled)**4 + 
                              np.cos(14 * np.pi * x_scaled)**4) * 
                             (1.0 + 0.5 * np.sin(10 * np.pi * x_scaled)))
        
        # Combine all terms with optimized weights
        return 0.25 * fractal_term + 0.25 * quantum_term + 0.2 * penalty_term + 0.2 * radial_term + 0.1 * coupled_term