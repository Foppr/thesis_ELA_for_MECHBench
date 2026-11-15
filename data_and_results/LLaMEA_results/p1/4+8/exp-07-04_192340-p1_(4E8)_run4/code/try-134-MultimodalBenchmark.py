import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Additional chaotic parameters for enhanced complexity
        self.chaotic_params = np.random.uniform(0.5, 2.0, dim)
        self.penalty_weights = np.random.uniform(0.001, 0.01, dim)
    
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
            freq1 = (i + 1) * np.pi / 3
            freq2 = (i + 1) * np.pi / 5
            result += 3 * np.sin(x_rot[i] * freq1) * np.cos(x_rot[i] * freq2)
            # Enhanced logarithmic barrier to prevent divergence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 2)
            result += log_term * (i + 1) * 0.1
            # Chaotic component using a sine of sine transformation
            chaotic = np.sin(np.pi * np.sin(x_rot[i]))
            result += chaotic * (i + 1) * 0.05
            # Additional composite chaotic term with exponential decay
            exp_term = np.exp(-0.1 * np.abs(x_rot[i]))
            result += exp_term * np.sin(2 * np.pi * x_rot[i]) * (i + 1) * 0.02
            # New hyper-chaotic component with multiple sine waves
            hyper_chaotic = np.sin(x_rot[i] * self.chaotic_params[i]) * np.cos(x_rot[i] * self.chaotic_params[i] * 0.5)
            result += hyper_chaotic * (i + 1) * 0.03
            # Additional cubic term for increased nonlinearity
            result += 0.01 * (x_rot[i] ** 3) * np.sin(x_rot[i] * 0.5)
        
        # Enhanced penalty term for large values with adaptive scaling
        penalty = 0.001 * np.sum(np.abs(x_rot) ** 3)
        # Add curvature-based adaptive penalty
        curvature_penalty = 0.0001 * np.sum((x_rot ** 2) * np.abs(x_rot))
        # Add a novel hybrid penalty that combines multiple penalty types
        hybrid_penalty = 0.0005 * np.sum(np.exp(np.abs(x_rot)) - 1)
        # Add a noise injection term to increase robustness testing
        noise = 0.0001 * np.sum(np.sin(x_rot * 10) * np.cos(x_rot * 7))
        result += penalty + curvature_penalty + hybrid_penalty + noise
        
        return result