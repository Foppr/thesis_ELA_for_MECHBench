import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute a more complex rotation matrix with orthogonalization
        self.rotation = np.random.rand(dim, dim)
        self.rotation = np.linalg.qr(self.rotation)[0]
        # Add a non-uniform shift to increase asymmetry
        self.shift = np.random.uniform(-1.0, 1.0, dim)
        # Add a scaling factor per dimension for increased complexity
        self.scaling = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation, shift, and scaling
        x_scaled = self.scaling * (np.dot(self.rotation, x) + self.shift)
        
        # Compute the multimodal function with enhanced chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients and exponential decay
            quadratic = (x_scaled[i] ** 2) * (i + 1) * 0.3
            exponential_decay = np.exp(-0.1 * np.abs(x_scaled[i]))
            result += quadratic * exponential_decay
            
            # Sinusoidal components with varying frequencies, amplitudes, and phases
            freq = (i + 1) * np.pi / 2
            amp = 2.0 + np.sin(i)
            phase = np.cos(i * np.pi / 4)
            sinusoidal = amp * np.sin(freq * x_scaled[i] + phase)
            result += sinusoidal
            
            # Enhanced logarithmic barrier with a double-log structure
            log_barrier = np.log(1 + np.abs(x_scaled[i]) ** 3) * np.log(1 + np.abs(x_scaled[i]))
            result += log_barrier * (i + 1) * 0.15
            
            # Chaotic component with a tent map-like structure
            tent_map = 1 - 2 * np.abs(x_scaled[i] - np.floor(x_scaled[i] + 0.5))
            chaotic = np.sin(np.pi * tent_map * np.sin(x_scaled[i]))
            result += chaotic * (i + 1) * 0.08
        
        # Add a hybrid penalty mechanism combining curvature and gradient-based penalties
        hybrid_penalty = 0.0
        for i in range(self.dim):
            # Estimate local curvature using finite differences
            h = 1e-3
            second_diff = (np.sin(x_scaled[i] + h) - 2 * np.sin(x_scaled[i]) + np.sin(x_scaled[i] - h)) / (h ** 2)
            curvature_term = np.abs(second_diff) * (i + 1) * 0.02
            
            # Gradient-based penalty using a smoothed version of the gradient
            grad = np.cos(x_scaled[i]) * (i + 1) * np.pi / 2
            gradient_term = np.abs(grad) * (i + 1) * 0.01
            
            # Combine both penalties with a nonlinear function
            hybrid_penalty += (curvature_term + gradient_term) * np.exp(-0.05 * np.abs(x_scaled[i]))
        
        result += hybrid_penalty
        
        # Add a global noise term to increase robustness testing
        noise = np.sum(np.random.normal(0, 0.01, self.dim) * np.sin(x_scaled))
        result += noise
        
        return result