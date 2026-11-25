import numpy as np

class InterferenceHillBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.5 + 0.5 * np.cos(i * 0.3)
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Polynomial coupling terms with exponential decay
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                weight = 1.0 / (1.0 + np.abs(i - j)**1.5)
                poly_term = x_scaled[i]**2 + x_scaled[j]**2 + 0.5 * x_scaled[i] * x_scaled[j]
                poly_coupling += weight * poly_term * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Exponentially decaying Gaussian hills with random positions and heights
        gaussian_hills = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.8) * 0.8
            height = 1.0 + 0.5 * np.cos(i * 0.6)
            width = 0.3 + 0.2 * np.sin(i * 0.4)
            gaussian_hills += height * np.exp(-0.5 * ((x_scaled[i] - center)**2) / (width**2))
        
        # Interference pattern from multiple sine waves with phase shifts
        interference = 0.0
        for i in range(self.dim):
            for k in range(1, 6):
                phase_shift = np.sin(i * 0.3 + k * 0.2)
                interference += np.sin(k * x_scaled[i] + phase_shift) * np.cos(k * x_scaled[i] * 0.8 + phase_shift)
        
        # Cross-dimensional interaction with cosine modulation and exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 2.0 / (1.0 + np.abs(i - j)**2.0)
                modulator = np.cos(0.5 * x_scaled[i] + 0.3 * x_scaled[j])
                cross_interaction += weight * modulator * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Combined function with carefully tuned weights for maximum complexity
        return 1.5 * periodic + 1.8 * poly_coupling + 1.2 * gaussian_hills + 0.9 * interference + 1.4 * cross_interaction