import numpy as np

class QuaternionGaussianCouplingLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Quaternion rotation components for high-dimensional complexity
        self.quaternion_angles = np.random.rand(dim // 2 + 1) * 2.0 * np.pi if dim % 2 == 0 else np.random.rand(dim // 2) * 2.0 * np.pi
        # Gaussian peak centers and amplitudes with dynamic scaling
        self.peak_centers = 4.0 * np.random.rand(dim, 15) - 2.0
        self.peak_amplitudes = 2.0 + 8.0 * np.random.rand(15)
        self.peak_widths = 0.2 + 1.8 * np.random.rand(15)
        # Adaptive conditioning with exponential and logarithmic components
        self.conditioning_exp = 1.0 + 3.0 * np.random.rand(dim)
        self.conditioning_log = 0.5 + 2.0 * np.random.rand(dim)
        # Non-linear coupling terms with varying interaction strengths
        self.coupling_strengths = 0.5 + 4.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 0.3 + 3.0 * np.random.rand(dim, dim)
        # Dynamic bias components for deceptive behavior
        self.bias_magnitude = 1.5 + 3.0 * np.random.rand()
        self.bias_directions = np.random.choice([-1, 1], size=(dim, 5))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quaternion-based rotation component
        rot_component = 0.0
        if self.dim >= 4:
            # Simplified quaternion rotation effect using 2D rotation blocks
            for i in range(0, min(self.dim, 4), 2):
                if i + 1 < self.dim:
                    angle = self.quaternion_angles[i // 2] if i // 2 < len(self.quaternion_angles) else 0.0
                    rot_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
                    vec = np.array([x_norm[i], x_norm[i+1]])
                    rotated = np.dot(rot_matrix, vec)
                    rot_component += 0.2 * (rotated[0]**3 + rotated[1]**3)
        
        # Gaussian peaks with dynamic widths and amplitudes
        peak_sum = 0.0
        for k in range(15):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.peak_centers[i, k])**2
            peak_sum += self.peak_amplitudes[k] * np.exp(-dist / (2.0 * self.peak_widths[k]**2))
        
        # Adaptive conditioning with exponential and logarithmic terms
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_exp[i] * (np.exp(np.abs(x_norm[i])) - 1.0) + \
                        self.conditioning_log[i] * np.log(1.0 + np.abs(x_norm[i]))
        
        # Non-linear coupling terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
        
        # Dynamic bias term
        bias_sum = 0.0
        for i in range(self.dim):
            for k in range(5):
                bias_sum += self.bias_magnitude * self.bias_directions[i, k] * np.sin(2.0 * np.pi * x_norm[i])
        
        # Combine all components with weighted contributions
        result = 0.25 * peak_sum + 0.20 * cond_sum + 0.18 * coupling_sum + 0.15 * rot_component + 0.22 * bias_sum
        
        # Add penalty for large values and oscillatory behavior
        penalty = 0.15 * np.sum(np.abs(x_norm)**6) + 0.10 * np.sum(np.sin(8.0 * x_norm))
        
        return result + penalty