import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with varying width and amplitude
        rbf = 0.0
        for i in range(self.dim):
            # Dimensionally varying widths and amplitudes
            width = 0.5 + 0.3 * np.sin(i * 0.5)
            amplitude = 1.0 + 0.5 * np.cos(i * 0.3)
            rbf += amplitude * np.exp(-0.5 * (x_norm[i] / width)**2)
        
        # Harmonic potential component with dimensionally varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.4) + 0.5 * np.cos(i * 0.7)
            harmonic += 0.5 * freq * (x_norm[i]**2 - 2.0 * x_norm[i] * np.sin(freq * x_norm[i]))
        
        # Stochastic noise injection with dimensionally varying intensity
        noise = 0.0
        for i in range(self.dim):
            noise_intensity = 0.1 + 0.05 * np.sin(i * 0.6)
            noise += noise_intensity * np.random.normal(0, 1)
        
        # Cross-dimensional coupling with exponential interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = 0.3 + 0.2 * np.sin((i+j) * 0.5)
                cross += coupling_strength * np.exp(-dist**2 * (1.0 + 0.2 * i))
        
        # Dimensionality-dependent scaling factor
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3)
        
        # Combine all components with dynamic weights
        weight_rbf = 0.4 + 0.1 * np.sin(self.dim * 0.2)
        weight_harmonic = 0.3 + 0.15 * np.cos(self.dim * 0.15)
        weight_noise = 0.2 + 0.05 * np.tanh(self.dim * 0.1)
        weight_cross = 0.1
        
        return scale_factor * (weight_rbf * rbf + 
                              weight_harmonic * harmonic + 
                              weight_noise * noise + 
                              weight_cross * cross)