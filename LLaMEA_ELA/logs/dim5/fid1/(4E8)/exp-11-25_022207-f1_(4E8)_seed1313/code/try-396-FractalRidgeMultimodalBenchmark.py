import numpy as np

class FractalRidgeMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal Gaussian parameters with varying scales
        self.gaussian_scales = np.logspace(0.5, 3.0, min(20, dim))
        self.gaussian_amplitudes = np.random.uniform(1.0, 3.0, min(20, dim))
        # Ridge structure parameters with dynamic scaling
        self.ridge_heights = np.random.uniform(0.5, 2.0, min(15, dim))
        self.ridge_widths = np.logspace(-1.0, 1.5, min(15, dim))
        # Adaptive conditioning gradients
        self.conditioning_strengths = np.linspace(1.0, 10.0, min(25, dim))
        # Cross-dimensional interaction parameters
        self.interaction_coefficients = np.random.uniform(0.1, 0.8, min(25, dim))
        # Fractal dimension scaling for ridge structures
        self.fractal_dimensions = np.random.uniform(0.3, 1.2, min(20, dim))
        # Dynamic noise modulation
        self.noise_amplitudes = np.random.uniform(0.05, 0.3, min(15, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal Gaussian components with varying scales
        gaussian_term = 0.0
        for i in range(min(len(self.gaussian_scales), self.dim)):
            scale = self.gaussian_scales[i]
            amplitude = self.gaussian_amplitudes[i]
            # Fractal Gaussian with sinusoidal modulation
            gaussian_term += amplitude * np.exp(-0.5 * (x_norm[i] / scale) ** 2) * (
                1.0 + 0.3 * np.sin(5.0 * x_norm[i]) * np.cos(3.0 * x_norm[i])
            )
            
        # Dynamic ridge structures with fractal scaling
        ridge_term = 0.0
        for i in range(min(len(self.ridge_heights), self.dim)):
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            fractal_dim = self.fractal_dimensions[i]
            # Ridge with hyperbolic tangent shaping
            ridge_term += height * np.tanh(x_norm[i] / width) ** fractal_dim
            
        # Adaptive conditioning with exponential scaling
        condition_term = 0.0
        for i in range(min(len(self.conditioning_strengths), self.dim)):
            strength = self.conditioning_strengths[i]
            # Exponential and polynomial conditioning
            condition_term += strength * (np.exp(0.2 * np.abs(x_norm[i])) - 1.0) + \
                             0.3 * strength * x_norm[i] ** 4
            
        # Cross-dimensional interaction with ridge coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coeff = self.interaction_coefficients[i % len(self.interaction_coefficients)]
                # Coupled ridge interactions with fractal modulation
                interaction_term += coeff * (
                    np.tanh(x_norm[i] / (self.ridge_widths[i % len(self.ridge_widths)])) * 
                    np.tanh(x_norm[j] / (self.ridge_widths[j % len(self.ridge_widths)]))
                ) * np.sin(2.0 * (x_norm[i] + x_norm[j]))
                
        # Dynamic noise component with fractal modulation
        noise_term = 0.0
        for i in range(min(len(self.noise_amplitudes), self.dim)):
            amplitude = self.noise_amplitudes[i]
            # Fractal noise with multiple frequency components
            noise_term += amplitude * (
                np.sin(10.0 * x_norm[i]) + 
                0.5 * np.sin(20.0 * x_norm[i]) + 
                0.3 * np.sin(30.0 * x_norm[i])
            )
            
        # Combined landscape with dynamic weighting
        result = 0.4 * gaussian_term + 0.3 * ridge_term + 0.2 * condition_term + 0.08 * interaction_term + 0.02 * noise_term
        
        return result