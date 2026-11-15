import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic behavior
        self.chaos_seq = np.sin(np.arange(dim) * np.pi / (dim + 1)) * np.exp(-np.arange(dim) / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Dynamic chaotic sine-cosine interactions
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                chaotic_interaction += self.chaos_seq[i] * self.chaos_seq[j] * np.sin(dist * np.pi) * np.cos(dist * 2 * np.pi)
        
        # Adaptive noise perturbation with dynamic amplitude
        noise_amp = 0.5 * (1.0 + np.sin(np.sum(x**2) / (self.dim * 10.0)))
        noise = noise_amp * np.sum(np.random.randn(self.dim) * np.exp(-0.1 * np.abs(x)))
        
        # Multi-scale multimodal peaks using Gaussian and polynomial combinations
        peaks = 0.0
        scales = [0.5, 1.0, 2.0, 3.0]
        for scale in scales:
            peaks += np.sum(np.exp(-0.5 * ((x / scale)**2)) * np.cos(scale * x)**2)
        
        # Dynamic polynomial coupling with time-varying exponents
        poly_coupling = 0.0
        for i in range(self.dim - 1):
            exp_factor = 1.0 + 0.2 * np.sin(self.chaos_seq[i] * 10.0)
            poly_coupling += (x[i]**exp_factor - x[i+1]**exp_factor)**2
        
        # Saddle point landscape with varying curvature
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2.0 * x[i]**2) * np.cos(x[i])
        
        # High-frequency oscillatory component with amplitude modulation
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(20.0 * x[i]) * np.cos(15.0 * x[i]) * (1.0 + 0.1 * np.sin(self.chaos_seq[i] * 5.0))
        
        # Combine all components
        result = result + chaotic_interaction + noise + peaks + poly_coupling + saddle + high_freq
        
        return result