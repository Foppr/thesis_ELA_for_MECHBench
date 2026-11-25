import numpy as np

class ChaoticGradientSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        scaled_x = x / 5.0
        
        # Base polynomial chaos term with dynamic exponents
        result = 0.0
        for i in range(self.dim):
            # Dynamic exponent based on dimension index
            exp = 2 + 2 * np.sin(i * np.pi / max(1, self.dim - 1))
            result += scaled_x[i]**exp
            
        # Add chaotic gradient components with varying coefficients
        gradient_penalty = 0.0
        for i in range(self.dim):
            # Chaotic coefficient variation
            coeff = 1.0 + 0.5 * np.sin(i * np.pi / max(1, self.dim - 1))
            gradient_penalty += coeff * scaled_x[i]**3
            
        result += gradient_penalty
        
        # Introduce saddle-point components with dynamic parameters
        saddle_penalty = 0.0
        for i in range(self.dim):
            # Saddle point parameters that vary with dimension
            a = 1.0 + 0.3 * np.sin(i * np.pi / max(1, self.dim - 1))
            b = 0.5 + 0.2 * np.cos(i * np.pi / max(1, self.dim - 1))
            
            # Saddle contribution
            saddle_term = a * scaled_x[i]**2 - b * scaled_x[i]**4
            saddle_penalty += saddle_term
            
        result += saddle_penalty
        
        # Add dynamic coupling between dimensions with varying strength
        coupling_penalty = 0.0
        for i in range(self.dim):
            # Coupling with previous dimension
            if i > 0:
                coupling_strength = 0.3 + 0.7 * np.sin(i * np.pi / max(1, self.dim - 1))
                coupling_term = coupling_strength * (scaled_x[i] - scaled_x[i-1])**3
                coupling_penalty += coupling_term
                
            # Coupling with next dimension
            if i < self.dim - 1:
                coupling_strength = 0.3 + 0.7 * np.cos(i * np.pi / max(1, self.dim - 1))
                coupling_term = coupling_strength * (scaled_x[i] - scaled_x[i+1])**3
                coupling_penalty += coupling_term
                
        result += coupling_penalty
        
        # Add multi-modal Gaussian components for competing minima
        multimodal_penalty = 0.0
        num_gaussians = min(4, self.dim)
        for j in range(num_gaussians):
            center = np.sin(j * np.pi / max(1, num_gaussians - 1)) * 0.7
            amplitude = 1.5 + 0.5 * np.cos(j * np.pi / max(1, num_gaussians - 1))
            width = 0.2 + 0.1 * np.sin(j * np.pi / max(1, num_gaussians - 1))
            
            gaussian_sum = 0.0
            for i in range(self.dim):
                gaussian_sum += np.exp(-((scaled_x[i] - center)**2) / (2 * width**2))
                
            multimodal_penalty += amplitude * gaussian_sum
            
        result += multimodal_penalty
        
        # Add chaotic sinusoidal interaction terms between dimensions
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 3 + np.sin(i * j * np.pi / max(1, self.dim**2))
                coupling_term = np.sin(freq * scaled_x[i]) * np.cos(freq * scaled_x[j])
                chaotic_coupling += coupling_term
                
        result += 0.2 * chaotic_coupling
        
        # Add noise to increase non-smoothness
        noise = 0.1 * np.sum(np.sin(15 * scaled_x)**2 + np.cos(8 * scaled_x)**2)
        result += noise
        
        # Global scaling factor
        result *= (1.0 + 0.3 * self.dim)
        
        return result