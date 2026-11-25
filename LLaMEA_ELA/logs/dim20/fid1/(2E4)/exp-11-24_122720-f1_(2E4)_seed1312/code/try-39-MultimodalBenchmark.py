import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillation component with altered frequency scaling and cubic nonlinearity
        chaotic_osc = 0
        for i in range(self.dim):
            freq = (i + 1) * np.pi / (self.dim + 2)
            chaotic_osc += (np.sin(x[i] * freq) * np.cos(x[i] * freq * np.e) * 
                           np.exp(-0.03 * x[i]**2) * np.sin(3 * x[i] * freq) * np.abs(x[i])**1.5)
        
        # Multi-modal radial basis function with dynamic centers and adaptive widths
        rbf = 0
        for i in range(self.dim):
            center = 2 * np.sin(i * np.pi / 4) + 2 * np.cos(i * np.pi / 4)
            width = 0.25 + 0.15 * np.sin(i * np.pi / 5)
            rbf += np.exp(-0.5 * (x[i] - center)**2 / width) * (1 + 0.3 * np.sin(i * np.pi / 3))
        
        # Hybrid penalty term with both quartic and exponential components, plus a novel logarithmic correction
        hybrid_penalty = 0
        for i in range(self.dim):
            term1 = x[i]**4 - 6 * x[i]**3 + 11 * x[i]**2 - 6 * x[i]
            term2 = np.exp(-0.5 * x[i]**2) * np.sin(2 * x[i])
            log_corr = np.log(1 + 0.15 * np.abs(x[i]))
            hybrid_penalty += (term1**2 + 0.5 * term2**2 + 0.15 * log_corr)
        
        # Adaptive scaling factors based on dimensionality with additional sinusoidal modulation
        scale1 = 0.6 + 0.15 * np.sin(self.dim * np.pi / 12)
        scale2 = 0.5 + 0.25 * np.cos(self.dim * np.pi / 8)
        scale3 = 0.03 + 0.015 * np.sin(self.dim * np.pi / 6)
        
        # Combine all components with dynamic weighting and add a global shift
        return scale1 * chaotic_osc + scale2 * rbf + scale3 * hybrid_penalty + 4 * self.dim + 0.6 * np.sum(np.sin(x))