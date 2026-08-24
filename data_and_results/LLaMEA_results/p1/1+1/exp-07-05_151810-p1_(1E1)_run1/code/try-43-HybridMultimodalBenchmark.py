import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive polynomial weights with modified scaling
        poly_weights = 0.2 + 0.8 * np.sin(0.6 * np.arange(self.dim))
        result = np.sum(poly_weights * (0.4 * x**2 + 0.15 * x**3 + 0.02 * x**4))
        
        # Enhanced chaotic sine-wave coupling with increased modulation
        freq_mod = 2.5 + 2.5 * np.sin(0.4 * np.arange(self.dim))
        chaotic_coupling = np.sum(np.sin(freq_mod * x) * np.cos(freq_mod * x + np.pi/6) * np.exp(-0.15 * np.abs(x)))
        
        # Modified hyperbolic secant barrier with sharper transition
        sec_barrier = np.sum(2.0 * (1.0 / np.cosh(1.0 * x)) * np.exp(-0.3 * x**2))
        
        # Adjusted asymmetric exponential with modified decay
        asym_exp = np.sum(np.exp(-0.6 * x**2) * np.where(x >= 0, 1.5, 0.2) * np.cos(0.3 * x))
        
        # Refined multi-scale coupled sine waves with phase locking
        phase_lock = np.sin(x + 0.4 * np.cos(x)) * np.cos(1.5 * x + 0.2 * np.sin(x))
        multi_scale = np.sum(phase_lock * np.exp(-0.15 * np.abs(x)))
        
        # Improved tanh modulation with frequency-dependent gain
        tanh_mod = np.sum(np.tanh(1.5 * x) * np.sin(0.8 * x) * np.exp(-0.3 * x**2))
        
        # Modified quadratic coupling with spatially varying coefficients
        spatial_coupling = np.sum((x[:-1] - x[1:]) ** 2 * np.exp(-0.08 * np.abs(x[:-1] + x[1:])))
        
        # Adjusted logistic map component for better complexity balance
        logistic_map = np.sum(3.5 * x * (1.0 - x) * np.exp(-0.12 * np.abs(x)))
        
        # Combine all components
        result = result + chaotic_coupling + sec_barrier + asym_exp + multi_scale + tanh_mod + spatial_coupling + logistic_map
        
        return result