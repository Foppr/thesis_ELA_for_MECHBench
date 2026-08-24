import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with enhanced chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Enhanced sinusoidal components with varying frequencies and amplitudes
            freq1 = (i + 1) * np.pi / 2.5
            freq2 = (i + 1) * np.pi / 4.2
            result += 2.5 * np.sin(x_rot[i] * freq1) * np.cos(x_rot[i] * freq2)
            # Enhanced logarithmic barrier to prevent divergence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 1.8)
            result += log_term * (i + 1) * 0.12
            # Chaotic component using a sine of sine transformation
            chaotic = np.sin(np.pi * np.sin(x_rot[i]))
            result += chaotic * (i + 1) * 0.06
            # Additional composite chaotic term with exponential decay
            exp_term = np.exp(-0.15 * np.abs(x_rot[i]))
            result += exp_term * np.sin(2.5 * np.pi * x_rot[i]) * (i + 1) * 0.025
            # Additional sine-wave interaction term
            result += 0.3 * np.sin(3 * x_rot[i]) * np.cos(0.5 * x_rot[i]) * (i + 1) * 0.03
        
        # Enhanced penalty term for large values with adaptive scaling
        penalty = 0.0015 * np.sum(np.abs(x_rot) ** 3.2)
        # Add curvature-based adaptive penalty
        curvature_penalty = 0.0002 * np.sum((x_rot ** 2) * np.abs(x_rot))
        # Add a novel hybrid penalty based on gradient magnitude
        grad_magnitude = np.sum(np.abs(np.gradient(x_rot)))
        hybrid_penalty = 0.0005 * grad_magnitude ** 2
        result += penalty + curvature_penalty + hybrid_penalty
        
        return result