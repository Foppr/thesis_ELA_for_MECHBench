import numpy as np

class GradientMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize gradient parameters for each dimension
        self.gradient_magnitude = np.random.uniform(1.0, 3.0, dim)
        self.gradient_direction = np.random.uniform(-1.0, 1.0, dim)
        self.bias_field_strength = np.random.uniform(0.5, 2.0, dim)
        # Saddle point distribution parameters
        self.saddle_count = max(1, dim // 3)
        self.saddle_positions = np.random.uniform(-5.0, 5.0, (self.saddle_count, dim))
        self.saddle_strengths = np.random.uniform(1.0, 4.0, self.saddle_count)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Gradient-based terrain with directional bias
        gradient_term = 0.0
        for i in range(self.dim):
            grad_component = self.gradient_magnitude[i] * x_norm[i] * np.exp(-0.5 * (x_norm[i] ** 2))
            bias_component = self.bias_field_strength[i] * np.sin(2 * np.pi * x_norm[i])
            gradient_term += grad_component + bias_component
        
        # Multi-modal energy wells with varying depths and widths
        modal_term = 0.0
        for i in range(self.dim):
            well_depth = 2.0 + 3.0 * np.sin(0.5 * x_norm[i] + i)
            well_width = 0.5 + 0.5 * np.cos(0.3 * x_norm[i] + i)
            modal_term += well_depth * np.exp(-0.5 * (x_norm[i] ** 2) / (well_width ** 2))
        
        # Saddle point interactions
        saddle_term = 0.0
        for i in range(self.saddle_count):
            dist = np.sum((x_norm - self.saddle_positions[i]) ** 2)
            saddle_term += self.saddle_strengths[i] * np.exp(-dist / (2.0 * 0.5 ** 2))
        
        # Directional correlation and coupling
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_strength = 0.3 * np.sin(0.2 * (x_norm[i] + x_norm[j]))
                corr_term += corr_strength * np.exp(-0.2 * (x_norm[i] - x_norm[j]) ** 2)
        
        # Combined fitness
        combined = gradient_term + modal_term - saddle_term + corr_term
        
        # Add stochastic noise and scaling
        noise = 0.01 * np.random.normal(0, 1)
        scale_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm))
        
        return combined * scale_factor + noise