import numpy as np

class ExponentialTrigonometricSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential barrier parameters
        self.barrier_centers = -2.0 + 4.0 * np.random.rand(dim)
        self.barrier_heights = 1.0 + 3.0 * np.random.rand(dim)
        self.barrier_widths = 0.5 + 2.0 * np.random.rand(dim)
        # Trigonometric coupling coefficients
        self.coupling_amplitudes = 0.5 + 2.5 * np.random.rand(dim, dim)
        self.coupling_frequencies = 1.0 + 6.0 * np.random.rand(dim, dim)
        # Saddle point parameters
        self.saddle_positions = 2.5 * np.random.rand(dim, 8) - 1.25
        self.saddle_strengths = 0.5 + 2.0 * np.random.rand(8)
        # Asymmetric polynomial terms
        self.poly_exponents = 2.0 + 4.0 * np.random.rand(dim)
        self.poly_coefficients = 0.3 + 1.7 * np.random.rand(dim)
        # Global rotation matrix
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        # Conditioning and scaling parameters
        self.conditioning_factors = 0.5 + 2.5 * np.random.rand(dim)
        self.scaling_factors = 1.0 + 2.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            barrier_sum += self.barrier_heights[i] * np.exp(-0.5 * (dist / self.barrier_widths[i])**2)
        
        # Trigonometric coupling component
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_amplitudes[i, j] * np.sin(self.coupling_frequencies[i, j] * x_norm[i]) * np.cos(x_norm[j])
        
        # Saddle point attraction
        saddle_sum = 0.0
        for k in range(8):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.saddle_positions[i, k])**2
            saddle_sum += self.saddle_strengths[k] * np.exp(-dist / 2.0)
        
        # Asymmetric polynomial component
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Combine all components with varying weights
        result = 0.25 * barrier_sum + 0.30 * coupling_sum + 0.25 * saddle_sum + 0.20 * poly_sum
        
        # Add rotation and conditioning effects
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.1 * (rotated[0]**2 + rotated[1]**2)
        
        # Adaptive conditioning and scaling
        conditioning_term = 0.0
        for i in range(self.dim):
            conditioning_term += self.conditioning_factors[i] * np.log(1.0 + self.scaling_factors[i] * np.abs(x_norm[i]))
        
        result += 0.15 * conditioning_term
        
        # Global penalty term with enhanced nonlinearity
        penalty = 0.1 * np.sum(np.abs(x_norm)**3.5)
        
        return result + penalty