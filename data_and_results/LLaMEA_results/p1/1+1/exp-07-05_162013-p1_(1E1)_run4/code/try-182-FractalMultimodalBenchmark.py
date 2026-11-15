import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dimension = 1.5 + 0.5 * np.random.rand()
        self.scale_factors = np.random.rand(dim) * 2 + 1
        self.rotation_matrices = []
        for i in range(dim // 2 + 1):
            angle = np.random.rand() * 2 * np.pi
            rot = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
            if i * 2 < dim:
                full_rot = np.eye(dim)
                full_rot[i*2:(i*2)+2, i*2:(i*2)+2] = rot
                self.rotation_matrices.append(full_rot)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Base quadratic term
        result += 0.1 * np.sum(x**2)
        
        # Fractal-like multimodal components with varying scales
        for i in range(self.dim):
            scale = self.scale_factors[i]
            # Multi-scale sinusoidal modulations
            for k in range(1, 6):
                freq = k * scale
                result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
                result += 0.3 * np.sin(freq * x[i] * 2) * np.cos(freq * x[i] * 1.5)
        
        # Self-similar interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-invariant interaction with fractal scaling
                dist = np.abs(x[i] - x[j])
                interaction = 0.2 * np.sin(dist * 10) * np.cos(dist * 5)
                result += interaction * (1 + 0.1 * np.sin(self.fractal_dimension * dist))
        
        # Rotated fractal components
        for rot_mat in self.rotation_matrices:
            rotated_x = rot_mat @ x
            for i in range(len(rotated_x)):
                result += 0.1 * np.sin(rotated_x[i] * 3) * np.cos(rotated_x[i] * 2)
        
        # Multi-fractal basin structure
        basin_penalty = 0.0
        for i in range(self.dim):
            basin_penalty += 0.05 * np.sin(x[i] * 20) * np.cos(x[i] * 15)
        result += basin_penalty
        
        # Scale-invariant noise with fractal characteristics
        noise = 0.02 * np.sum(np.sin(x * 100) * np.cos(x * 50))
        result += noise
        
        # Add fractal dimension scaling factor
        result *= (1 + 0.05 * self.fractal_dimension)
        
        return result