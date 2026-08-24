import numpy as np

class ChaoticCrossDimBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Generate chaotic rotation matrix for cross-dimension coupling
        self.rotation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                self.rotation_matrix[i, j] = np.sin(i * j * 0.1 + np.random.rand() * 0.5) + np.cos(i * j * 0.15 + np.random.rand() * 0.3)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Apply chaotic rotation for cross-dimension coupling
        x_rotated = self.rotation_matrix @ x
        
        # Multi-scale chaotic landscape with nested optima
        result = 0.0
        
        # Base chaotic component with multiple frequencies
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(0.3 * i)
            freq2 = 1.0 + 0.3 * np.cos(0.4 * i)
            freq3 = 1.0 + 0.4 * np.sin(0.5 * i)
            result += np.sin(freq1 * x_rotated[i]) * np.cos(freq2 * x_rotated[i]**2) * np.sin(freq3 * x_rotated[i]**3)
        
        # Add nested chaotic modulations with varying scales
        for i in range(self.dim):
            scale = 0.5 + 0.5 * np.sin(0.2 * i)
            modulation = np.sin(3.0 * x_rotated[i] + 0.5 * i) * np.cos(2.0 * x_rotated[i] + 0.3 * i)
            result += scale * modulation * np.exp(-0.1 * np.abs(x_rotated[i]))
        
        # Dynamic conditioning based on dimension and chaotic factor
        condition_factor = 1.0 + 0.3 * np.sin(0.1 * self.dim) * np.cos(0.05 * self.dim)
        result *= condition_factor
        
        # Add multi-modal component with chaotic centers
        multimodal = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.4 * i) + 0.5 * np.cos(0.3 * i)
            width = 0.5 + 0.3 * np.sin(0.2 * i)
            amplitude = 1.0 + 0.4 * np.cos(0.5 * i)
            multimodal += amplitude * np.exp(-0.5 * ((x_rotated[i] - center) / width)**2)
        
        # Combine base and multimodal components
        result += 0.5 * multimodal
        
        # Add boundary penalty with chaotic perturbations
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_rotated[i])
            if dist_from_bound < 0:
                chaotic_factor = 1.0 + 0.2 * np.sin(0.3 * i) + 0.1 * np.cos(0.2 * i)
                boundary_penalty += 5.0 * np.exp(-dist_from_bound**2) * chaotic_factor
        result += boundary_penalty
        
        # Add global scaling and chaotic noise
        global_scale = 1.0 + 0.2 * np.sin(0.1 * self.dim)
        result *= global_scale
        
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(4.0 * x_rotated[i] + 0.2 * i) * np.cos(3.0 * x_rotated[i] + 0.1 * i)
        result += noise
        
        return result