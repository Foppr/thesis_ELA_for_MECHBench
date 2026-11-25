import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 3.95
        self.sigma = 0.1
        self.alpha = 2.0
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaotic component
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = 0.5
        for i in range(1, self.dim):
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1])
        
        # Radial basis function with chaotic modulation
        rbfs = np.sum(np.exp(-self.alpha * (x_scaled - chaotic_seq)**2))
        
        # Trigonometric chaos with varying frequencies
        trig_chaos = np.sum(np.sin(self.r * x_scaled + chaotic_seq) * 
                           np.cos(self.r * x_scaled**2 + chaotic_seq) + 
                           0.5 * np.sin(self.r * x_scaled**3 + chaotic_seq))
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = np.sum(np.sin(x_scaled[:-1] * x_scaled[1:] + chaotic_seq[:-1]) * 
                               np.cos(x_scaled[:-1] + x_scaled[1:] + chaotic_seq[1:]))
        
        # Multi-scale chaotic interference
        multi_scale = np.sum(np.sin(2.0 * x_scaled * chaotic_seq) * 
                            np.cos(3.0 * x_scaled**2 * chaotic_seq) + 
                            0.3 * np.sin(5.0 * x_scaled**3 * chaotic_seq))
        
        # Asymmetric chaotic landscape
        asym_chaos = np.sum(np.exp(-np.abs(x_scaled)) * np.sin(self.r * x_scaled + chaotic_seq) + 
                           0.7 * np.exp(-np.abs(x_scaled)**2) * np.cos(self.r * x_scaled**2 + chaotic_seq))
        
        # Combine all components with dynamic weights
        return (1.5 * rbfs + 1.2 * trig_chaos + 0.8 * cross_coupling + 
                0.6 * multi_scale + 0.9 * asym_chaos + 2.1)