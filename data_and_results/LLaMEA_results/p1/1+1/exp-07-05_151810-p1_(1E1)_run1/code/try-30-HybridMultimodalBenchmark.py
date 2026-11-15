import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with increased higher-order terms and altered weights
        result = np.sum(0.5 * x**2 + 0.2 * x**3 + 0.05 * x**4 + 0.005 * x**5)
        
        # Enhanced trigonometric components with multiple frequencies and coupling
        trig_term = np.sum(np.sin(5.0 * x) * np.cos(6.0 * x) * np.tan(0.5 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Stronger logarithmic barrier with additional exponential scaling
        log_barrier = np.sum(2.0 * np.log(1.0 + 0.5 * np.abs(x)) * np.exp(-0.3 * x**2) * np.sin(0.2 * x))
        
        # Asymmetric exponential decay with multi-scale modulation
        asym_exp = np.sum(np.exp(-0.5 * x**2) * np.where(x >= 0, 1.5, 0.2) * np.cos(2.0 * x))
        
        # Coupled sine waves with dynamic phase shifts and dimension interaction
        phase_shifts = np.arange(self.dim) * np.pi / 4.0
        coupled_sine = np.sum(np.sin(x + phase_shifts) * np.cos(4.0 * x + phase_shifts) * np.exp(-0.1 * np.abs(x)))
        
        # Hyperbolic tangent modulation with variable strength and cross-term interactions
        tanh_mod = np.sum(np.tanh(1.5 * x) * np.sin(0.5 * x) * np.cos(0.3 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Cross-dimensional interaction terms with exponential coupling
        cross_terms = np.sum(np.exp(-0.1 * np.abs(x - np.roll(x, 1))) * np.sin(x + np.roll(x, 1)))
        
        # Additional high-frequency oscillatory component
        high_freq = np.sum(np.sin(10.0 * x) * np.cos(8.0 * x) * np.exp(-0.05 * x**2))
        
        # Add all components together
        result = result + trig_term + log_barrier + asym_exp + coupled_sine + tanh_mod + cross_terms + high_freq
        
        return result