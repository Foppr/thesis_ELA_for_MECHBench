import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quad_term = np.sum(0.5 * x**2)
        
        # Radial symmetry breaking with sinusoidal modulation
        radial_break = np.sum(np.sin(3.0 * np.sqrt(np.sum(x**2))) * np.cos(2.0 * np.sqrt(np.sum(x**2))))
        
        # Chaotic saddle point component using hyperbolic tangent and exponential decay
        chaotic_saddle = np.sum(np.tanh(2.5 * x) * np.exp(-0.3 * x**2) * np.sin(4.0 * x))
        
        # Adaptive cross-dimensional coupling with varying interaction strengths
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (x[i] * np.sin(2.0 * x[i+1]) + x[i+1] * np.cos(1.5 * x[i])) * (1.0 + 0.1 * np.sin(i))
        
        # High-frequency oscillation with amplitude modulation
        high_freq = np.sum(np.sin(10.0 * x) * np.cos(8.0 * x) * (1.0 + 0.2 * np.sin(5.0 * x)))
        
        # Multimodal component with multiple local minima
        multimodal = np.sum(0.3 * np.sin(6.0 * x) * np.cos(4.0 * x) * np.exp(-0.1 * x**2))
        
        # Combined function with optimized weights
        return 0.4 * quad_term + 0.3 * radial_break + 0.2 * chaotic_saddle + 0.05 * cross_coupling + 0.05 * high_freq + 0.05 * multimodal