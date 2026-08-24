import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_exponents = np.random.uniform(1.5, 3.5, dim)
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
        self.rotation_matrices = []
        for _ in range(dim):
            angle = np.random.uniform(0, 2*np.pi)
            matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            self.rotation_matrices.append(matrix)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Fractal polynomial components with varying exponents
        for i in range(self.dim):
            exponent = self.fractal_exponents[i]
            scale = self.scale_factors[i]
            # Base fractal term with power law scaling
            term = scale * (x[i]**exponent + 0.1 * np.sin(x[i] * 10) * np.cos(x[i] * 5))
            result += term
            
        # Multi-scale interaction terms with nested fractal structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal interaction with scale-dependent coupling
                scale_ij = (self.scale_factors[i] + self.scale_factors[j]) / 2
                interaction = scale_ij * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += interaction * (1 + 0.1 * np.sin(x[i] * 15) * np.cos(x[j] * 12))
                
        # Self-similar harmonic components
        for i in range(self.dim):
            # Add fractal harmonic series with decreasing amplitudes
            harmonic_sum = 0.0
            for k in range(1, 6):
                freq = k * (1 + 0.2 * np.sin(x[i] * k * 2))
                amp = 1.0 / (k ** 1.5)
                harmonic_sum += amp * np.sin(freq * x[i])
            result += harmonic_sum
            
        # Scale-invariant penalty with fractal dimension
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**2) * (1 + 0.05 * np.sin(x[i] * 20))
        result += penalty * (1 + 0.1 * np.sum(np.abs(x) ** 1.3))
        
        # Nested fractal coupling with rotation invariance
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                # Rotate coordinates for fractal coupling
                if j < self.dim:
                    rotated_i = x[i]
                    rotated_j = x[j]
                    # Simple 2D rotation
                    rot_matrix = self.rotation_matrices[i % len(self.rotation_matrices)]
                    coord = np.array([rotated_i, rotated_j])
                    rotated_coord = rot_matrix @ coord
                    rotated_i, rotated_j = rotated_coord[0], rotated_coord[1]
                    
                    # Fractal coupling with variable scaling
                    coupling = 0.05 * np.sin(rotated_i * rotated_j) * np.cos(rotated_i + rotated_j)
                    result += coupling * (1 + 0.02 * np.sin(rotated_i * 30))
        
        # Add fractal noise component
        noise = 0.03 * np.sum(np.sin(x * 25) * np.cos(x * 15))
        result += noise
        
        # Add fractal basin structure with multiple local minima
        basin_term = 0.0
        for i in range(self.dim):
            # Create fractal-like basin structure
            basin_term += 0.2 * np.sin(x[i] * 10) * np.cos(x[i] * 7) * np.sin(x[i] * 3)
        result += basin_term
        
        # Add scale-dependent complexity factor
        complexity_factor = 1.0 + 0.05 * np.sum(np.abs(x) ** 1.2)
        result *= complexity_factor
        
        return result