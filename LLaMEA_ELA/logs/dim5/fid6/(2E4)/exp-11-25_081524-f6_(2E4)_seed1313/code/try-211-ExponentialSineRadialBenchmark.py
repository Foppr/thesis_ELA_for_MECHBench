import numpy as np

class ExponentialSineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with time-varying rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.8 + 0.4 * np.sin(0.5 * self.t + i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(2.0 * x[i])
        
        # Sine-wave interference with dynamic frequencies and amplitudes
        sine_interference = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.2 * np.sin(0.6 * self.t + i * 0.4)
            amp = 0.7 + 0.3 * np.cos(0.5 * self.t + i * 0.5)
            sine_interference += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis function with time-varying centers and widths
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.4 * self.t + i * 0.6)
            width = 0.5 + 0.3 * np.cos(0.3 * self.t + i * 0.4)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional interactions with dynamic coupling strengths
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.6 + 0.4 * np.sin(0.7 * self.t + i * 0.5 + j * 0.4)
                cross_interaction += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Dynamic weighting with chaotic modulation
        w1 = 0.25 + 0.2 * np.sin(0.9 * self.t)
        w2 = 0.3 + 0.25 * np.cos(0.8 * self.t)
        w3 = 0.2 + 0.15 * np.sin(0.7 * self.t)
        w4 = 0.25 + 0.2 * np.cos(0.6 * self.t)
        
        # Combine all components
        result = w1 * exp_decay + w2 * sine_interference + w3 * rbf + w4 * cross_interaction
        
        # Apply dimensionality scaling with exponential growth factor
        if self.dim > 1:
            scale_factor = 1.0 + 0.15 * np.log(self.dim) + 0.01 * np.exp(0.1 * self.dim)
            result *= scale_factor
            
        return result