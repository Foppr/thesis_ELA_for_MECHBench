import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic perturbation
        quad_term = np.sum(x**2 * (1.0 + 0.3 * np.sin(3.0 * x)))
        
        # Multi-scale harmonic modulation with varying amplitudes
        harm_term = np.sum(np.sin(2.5 * x) * np.cos(1.7 * x) * np.sin(0.8 * x) * (1.0 + 0.2 * np.cos(4.0 * x)))
        
        # Saddle-point structure with exponential decay
        saddle_term = np.sum(np.exp(-0.5 * (x**2 - 1.0)**2) * (x**3 - 0.5 * x))
        
        # Non-linear coupling with asymmetric interaction
        coupling_term = np.sum((x[:-1]**2 + x[1:]**2) * np.sin(0.7 * x[:-1]) * np.cos(0.9 * x[1:]))
        
        # Fractal-like gradient modulation with recursive scaling
        grad_term = np.sum(np.abs(x)**(1.3 + 0.4 * np.cos(2.8 * x)) * np.sin(1.5 * x))
        
        # Chaotic phase interactions with time-delayed feedback
        phase_term = np.sum(np.sin(x - 0.3 * np.sin(2.0 * x)) * np.cos(x + 0.2 * np.cos(3.0 * x)))
        
        # High-frequency oscillation with amplitude and frequency modulation
        high_freq_term = np.sum(np.sin(6.0 * x) * np.cos(5.0 * x) * (1.0 + 0.15 * np.sin(3.5 * x)) * np.exp(-0.2 * x**2))
        
        # Combined function with weighted contributions
        return 0.3 * quad_term + 0.2 * harm_term + 0.15 * saddle_term + 0.15 * coupling_term + 0.1 * grad_term + 0.08 * phase_term + 0.07 * high_freq_term