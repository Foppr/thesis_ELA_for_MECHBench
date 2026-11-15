import numpy as np

class StructuredMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute random projections for cross-dimension interactions
        self.projection_matrix = np.random.randn(dim, dim)
        self.projection_matrix, _ = np.linalg.qr(self.projection_matrix)
        
        # Generate multiple local minima centers
        self.centers = np.random.uniform(-4.0, 4.0, (15, dim))
        
        # Generate random scales and rotations for each local minimum
        self.scales = np.random.uniform(0.5, 2.0, 15)
        self.rotations = []
        for _ in range(15):
            rot = np.random.randn(dim, dim)
            rot, _ = np.linalg.qr(rot)
            self.rotations.append(rot)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Apply random projection to induce cross-dimension coupling
        x_projected = self.projection_matrix @ x
        
        # Compute distance to each local minimum
        distances = []
        for i in range(15):
            center = self.centers[i]
            rotated_center = self.rotations[i] @ center
            dist = np.linalg.norm(x_projected - rotated_center)
            distances.append(dist)
        
        # Combine distances with exponential perturbations
        result = 0.0
        for i in range(15):
            dist = distances[i]
            # Exponential perturbation with chaotic modulation
            perturbation = np.exp(0.5 * np.sin(2.0 * dist)) * (1.0 + 0.3 * np.cos(3.0 * dist))
            # Combine with scale factor
            result += self.scales[i] * np.exp(-0.5 * (dist / (1.0 + 0.1 * dist))**2) * perturbation
        
        # Add chaotic harmonic components
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * i)
            amp = 0.8 + 0.2 * np.cos(0.2 * i)
            harmonic_sum += amp * np.sin(freq * x_projected[i]) * np.cos(freq * x_projected[i]**2)
        result += 0.5 * harmonic_sum
        
        # Add dynamic conditioning based on problem dimension
        condition_factor = 1.0 + 0.4 * np.sin(0.2 * self.dim) * np.cos(0.1 * self.dim)
        result *= condition_factor
        
        # Add boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x_projected[i])
            if dist_from_bound < 0:
                boundary_penalty += 10.0 * np.exp(-dist_from_bound**2)
        result += boundary_penalty
        
        # Add multi-scale periodic component
        periodic_component = 0.0
        for i in range(self.dim):
            period = 3.0 + 1.5 * np.sin(0.5 * i)
            periodic_component += 1.5 * np.sin(2.0 * np.pi * x_projected[i] / period)
        result += periodic_component
        
        return result