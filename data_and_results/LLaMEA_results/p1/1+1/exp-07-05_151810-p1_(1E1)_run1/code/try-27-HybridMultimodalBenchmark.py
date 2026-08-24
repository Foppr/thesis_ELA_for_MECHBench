import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with asymmetric weighting
        result = np.sum(0.5 * x**2 + 0.1 * x**3 + 0.02 * x**4)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Logarithmic barrier terms to penalize boundary proximity
        log_barrier = np.sum(np.log(1.0 + np.abs(x)) * np.exp(-0.05 * x**2))
        
        # Asymmetric exponential decay based on sign of variables
        asym_exp = np.sum(np.exp(-0.5 * x**2) * np.where(x >= 0, 1.0, 0.5))
        
        # Coupled sine waves with phase shifts
        phase_shifts = np.arange(self.dim) * np.pi / 4.0
        coupled_sine = np.sum(np.sin(x + phase_shifts) * np.cos(2.0 * x + phase_shifts))
        
        # Hyperbolic tangent modulation with variable strength
        tanh_mod = np.sum(np.tanh(x) * np.sin(0.5 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Add all components together
        result = result + trig_term + log_barrier + asym_exp + coupled_sine + tanh_mod
        
        return result