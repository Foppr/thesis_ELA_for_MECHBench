import numpy as np

class MultimodalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute peak locations and frequencies for sinusoidal modulations
        self.peaks = np.random.uniform(-4.5, 4.5, (10, dim))
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian peaks with exponentially decaying amplitudes
        result = 0.0
        for i in range(10):
            peak = self.peaks[i]
            amplitude = np.exp(-0.1 * i)
            distance = np.sum((x - peak)**2)
            result += amplitude * np.exp(-distance / 2.0)
        
        # Sinusoidal modulation to increase ruggedness
        sine_mod = 0.0
        for i in range(self.dim):
            sine_mod += np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Exponentially decaying harmonic terms to control conditioning
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += (np.sin(2 * self.frequencies[i] * x[i])**2 + 
                        np.cos(2 * self.frequencies[i] * x[i])**2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Asymmetric saddle-like interactions between dimensions
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += (x[i]**2 - x[i+1]**2) * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
        
        # Add a global scaling factor and combine components
        return 1.0 + 0.5 * sine_mod + 0.3 * harmonic + 0.4 * saddle - result