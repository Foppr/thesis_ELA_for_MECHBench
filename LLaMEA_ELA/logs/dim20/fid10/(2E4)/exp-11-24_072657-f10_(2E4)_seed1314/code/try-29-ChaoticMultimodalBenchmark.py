import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logarithmic barrier terms to create sharp gradients near boundaries
        barrier = np.sum(np.log(1.0 + np.abs(x_norm)) * (x_norm**2))
        
        # High-dimensional trigonometric coupling with chaotic frequency ratios
        freqs = np.arange(1, self.dim + 1) * np.pi * (1.0 + 0.1 * np.sin(x_norm))
        trig_coupling = np.sum(np.sin(freqs * x_norm)**2 * np.cos(freqs * x_norm)**2)
        
        # Saddle-point inducing polynomial with alternating signs
        saddle = np.sum((-1)**np.arange(self.dim) * (x_norm**4 - 2*x_norm**2 + 1))
        
        # Multi-scale interaction terms with varying powers
        scale_interaction = 0.0
        for i in range(self.dim - 1):
            scale_interaction += (x_norm[i] - x_norm[i+1])**6 + 0.5 * (x_norm[i]**3 - x_norm[i+1]**3)**2
            
        # Exponential decay with sinusoidal modulation
        modulated_exp = np.sum(np.exp(-x_norm**2) * np.sin(7 * x_norm) * np.cos(3 * x_norm))
        
        # Asymmetric cubic terms to break symmetry
        asym_cubic = np.sum(x_norm**3 * np.exp(-0.5 * x_norm**2))
        
        # Noise component for stochastic robustness testing
        noise = 0.005 * np.random.random()
        
        return 0.4 * barrier + 0.6 * trig_coupling + 0.3 * saddle + 0.5 * scale_interaction + 0.4 * modulated_exp + 0.3 * asym_cubic + noise