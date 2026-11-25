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
            # Slightly modified widths and amplitudes for more complexity
            width = 0.4 + 0.4 * np.sin(i * 0.6)
            amplitude = 1.2 + 0.3 * np.cos(i * 0.4)
            rbf += amplitude * np.exp(-0.5 * (x_norm[i] / width)**2)
        
        # Harmonic potential component with dimensionally varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            # Modified frequency modulation for increased ruggedness
            freq = 1.5 + 1.5 * np.sin(i * 0.5) + 0.3 * np.cos(i * 0.8)
            harmonic += 0.5 * freq * (x_norm[i]**2 - 2.0 * x_norm[i] * np.sin(freq * x_norm[i]))
        
        # Stochastic noise injection with dimensionally varying intensity
        noise = 0.0
        for i in range(self.dim):
            # Slightly increased noise intensity and changed modulation
            noise_intensity = 0.15 + 0.08 * np.sin(i * 0.7)
            noise += noise_intensity * np.random.normal(0, 1)
        
        # Cross-dimensional coupling with modified exponential interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                # Modified coupling strength with different modulation
                coupling_strength = 0.25 + 0.25 * np.sin((i+j) * 0.6)
                cross += coupling_strength * np.exp(-dist**2 * (1.2 + 0.1 * i))
        
        # Dimensionality-dependent scaling factor
        scale_factor = 1.0 + 0.15 * np.sin(self.dim * 0.4)
        
        # Combine all components with slightly adjusted weights
        weight_rbf = 0.35 + 0.12 * np.sin(self.dim * 0.25)
        weight_harmonic = 0.35 + 0.18 * np.cos(self.dim * 0.2)
        weight_noise = 0.2 + 0.08 * np.tanh(self.dim * 0.12)
        weight_cross = 0.15
        
        return scale_factor * (weight_rbf * rbf + 
                              weight_harmonic * harmonic + 
                              weight_noise * noise + 
                              weight_cross * cross)