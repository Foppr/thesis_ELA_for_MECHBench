import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create interaction between dimensions
        x_rotated = self.rotation_matrix @ x
        
        # Base quadratic term (ellipsoid shape)
        result = np.sum(x_rotated**2)
        
        # Add chaotic saddle points using sinusoidal and exponential components
        for i in range(self.dim):
            result += 20 * np.sin(0.7 * x_rotated[i]) * np.cos(1.3 * x_rotated[i]) * np.exp(-0.2 * np.abs(x_rotated[i]))
        
        # Add dynamic noise with varying frequency and amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 8 * np.sin(0.3 * x_rotated[i]**3) * np.cos(0.5 * x_rotated[i]**2) * np.exp(-0.1 * x_rotated[i]**2)
        
        result += noise
        
        # Add cross-dimension interactions with modified exponential decay and dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):  # Full interaction
                coupling = np.exp(-0.05 * (i - j)**2)  # Stronger coupling
                result += coupling * x_rotated[i] * x_rotated[j] * np.sin(0.4 * (x_rotated[i]**2 + x_rotated[j]**2))
        
        # Add a dynamic scaling factor based on the norm and trigonometric modulation
        norm = np.linalg.norm(x_rotated)
        dynamic_factor = 1.0 + 0.4 * np.sin(0.15 * norm) * np.cos(0.25 * norm)
        result *= dynamic_factor
        
        # Add a global exponential penalty to increase difficulty near boundaries
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 15 * np.exp(-0.5 * (np.abs(x_rotated[i]) - 5.0)**2)
        
        result += boundary_penalty
        
        # Add additional high-frequency periodic components for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 5 * np.sin(3.0 * x_rotated[i]) * np.cos(2.5 * x_rotated[i]) * np.exp(-0.3 * np.abs(x_rotated[i]))
        result += high_freq
        
        return result