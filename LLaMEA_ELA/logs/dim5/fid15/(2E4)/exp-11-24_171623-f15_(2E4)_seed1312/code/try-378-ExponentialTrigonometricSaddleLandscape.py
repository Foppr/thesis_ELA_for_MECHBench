import numpy as np

class ExponentialTrigonometricSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential barrier parameters with increased variability
        self.barrier_centers = -2.0 + 4.0 * np.random.rand(dim)
        self.barrier_heights = 2.0 + 4.0 * np.random.rand(dim)
        self.barrier_widths = 0.3 + 1.5 * np.random.rand(dim)
        # Trigonometric coupling coefficients with higher frequencies
        self.coupling_amplitudes = 1.0 + 3.0 * np.random.rand(dim, dim)
        self.coupling_frequencies = 4.0 + 10.0 * np.random.rand(dim, dim)
        # Saddle point parameters with increased complexity
        self.saddle_positions = 3.0 * np.random.rand(dim, 12) - 1.5
        self.saddle_strengths = 1.5 + 4.0 * np.random.rand(12)
        # Asymmetric polynomial terms with different exponents
        self.poly_exponents = 1.5 + 5.0 * np.random.rand(dim)
        self.poly_coefficients = 0.5 + 2.0 * np.random.rand(dim)
        # Global rotation matrix
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        
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
        for k in range(12):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.saddle_positions[i, k])**2
            saddle_sum += self.saddle_strengths[k] * np.exp(-dist / 1.5)
        
        # Asymmetric polynomial component
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Combine all components with varying weights
        result = 0.20 * barrier_sum + 0.35 * coupling_sum + 0.20 * saddle_sum + 0.25 * poly_sum
        
        # Add rotation and conditioning effects
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.15 * (rotated[0]**2 + rotated[1]**2)
        
        # Global penalty term with higher degree
        penalty = 0.15 * np.sum(np.abs(x_norm)**4)
        
        return result + penalty