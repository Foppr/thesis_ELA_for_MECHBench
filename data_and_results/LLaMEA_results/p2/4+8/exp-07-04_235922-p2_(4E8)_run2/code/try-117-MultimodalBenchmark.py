import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for global transformation
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        np.fill_diagonal(self.rotation_matrix, 0)
        self.rotation_matrix += np.eye(dim)
        self.rotation_matrix = self.rotation_matrix / np.linalg.norm(self.rotation_matrix, axis=1, keepdims=True)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply global rotation to x
        x_rotated = np.dot(self.rotation_matrix, x)
        
        # Enhanced chaotic multimodal components
        term1 = np.sum(x_rotated**2)
        term2 = 0.8 * np.sum(np.sin(7 * x_rotated) * np.cos(4 * x_rotated) * np.exp(-0.1 * np.abs(x_rotated)))
        term3 = 0.15 * np.sum(x_rotated**6 * np.sin(3 * x_rotated))
        term4 = 0.4 * np.sum(np.exp(-x_rotated**2) * np.sin(15 * x_rotated) * np.cos(5 * x_rotated))
        term5 = 0.08 * np.sum(np.abs(x_rotated) ** 4.2)
        term6 = 0.2 * np.sum(np.sin(x_rotated**3) * np.cos(x_rotated**2))
        
        # Add complex interaction terms between dimensions
        interaction = 0.03 * np.sum((x_rotated[:-1] - x_rotated[1:]) ** 3 * np.sin(7 * (x_rotated[:-1] + x_rotated[1:])))
        interaction += 0.01 * np.sum((x_rotated[:-2] - x_rotated[2:]) ** 2 * np.cos(4 * (x_rotated[:-2] + x_rotated[2:])))
        
        # Add a dynamic exponential barrier component
        barrier = 0.5 * np.sum(np.exp(-0.5 * (x_rotated - np.mean(x_rotated))**2) * np.sin(20 * x_rotated))
        
        # Add multi-scale sinusoidal modulation
        modulation = 0.3 * np.sum(np.sin(25 * x_rotated) * np.cos(10 * x_rotated) * np.exp(-0.05 * x_rotated**2))
        modulation += 0.2 * np.sum(np.sin(35 * x_rotated) * np.cos(15 * x_rotated) * np.exp(-0.02 * np.abs(x_rotated)))
        
        # Add higher-order coupling terms
        coupling = 0.1 * np.sum((x_rotated**3 - np.roll(x_rotated, 1)**3) * np.sin(5 * (x_rotated + np.roll(x_rotated, 1))))
        coupling += 0.05 * np.sum((x_rotated**4 - np.roll(x_rotated, 2)**4) * np.cos(3 * (x_rotated + np.roll(x_rotated, 2))))
        
        # Add saddle-point perturbations
        saddle = 0.02 * np.sum(np.sin(10 * x_rotated) * np.cos(10 * x_rotated) * (x_rotated**2 - 1)**2)
        
        # Add cross-terms for increased complexity
        cross_term = 0.01 * np.sum(x_rotated * np.sin(2 * x_rotated) * np.cos(3 * x_rotated))
        
        result = term1 + term2 + term3 + term4 + term5 + term6 + interaction + barrier + modulation + coupling + saddle + cross_term
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result