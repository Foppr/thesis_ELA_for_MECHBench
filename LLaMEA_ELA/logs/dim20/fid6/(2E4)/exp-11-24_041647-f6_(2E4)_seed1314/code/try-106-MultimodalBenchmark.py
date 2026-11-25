import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial term with chaotic varying degrees and adaptive coefficients
        poly_term = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4) + 0.5 * np.sin(i * 1.23)
            coeff = 1.0 / (1.0 + 0.2 * i + 0.1 * np.cos(i * 0.7))
            poly_term += coeff * (x_normalized[i] ** degree)
        
        # Trigonometric component with quantum-like interference and phase coupling
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (1 + 0.3 * np.sin(i * 0.4))
            amp = 1.0 + 0.2 * np.cos(i * 0.6)
            phase = 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(i * 0.9)
            trig_term += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] * 0.7 + phase)
        
        # Radial basis function component with fractal-like width variation
        radial_term = 0.0
        for i in range(self.dim):
            width = 0.3 + 0.4 * (1 + np.sin(i * 0.5)) * (1 + np.cos(i * 0.3))
            radial_term += np.exp(-0.5 * (x_normalized[i] / width) ** (2 + 0.3 * np.sin(i * 0.4)))
        
        # Cross-dimensional interaction with chaotic coupling strength and fractal curvature
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + 0.3 * np.abs(x_normalized[i] - x_normalized[j]) + 0.1 * np.sin(i * j * 0.5))
                curvature = 1.0 + 0.2 * np.cos(i * j * 0.3)
                interaction_term += coupling * (x_normalized[i] ** 2 * curvature + x_normalized[j] ** 2 * curvature)
        
        # Quantum-inspired noise component with chaotic frequency modulation
        noise_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.4 * np.sin(i * 0.6 + 0.3 * np.cos(i * 0.8))
            phase_mod = 0.2 * np.sin(i * 0.9 + 0.5 * np.cos(i * 0.7))
            noise_term += (np.sin(freq_mod * x_normalized[i] + phase_mod) * 
                          np.cos(freq_mod * x_normalized[i] * 0.8 + phase_mod) * 
                          (1.0 - 0.15 * i + 0.05 * np.sin(i * 0.5)))
        
        # Fractal-like adaptive weighting with chaotic modulation
        weights = []
        for i in range(5):
            w = 0.2 + 0.1 * np.sin(i * 1.5 + 0.3 * np.cos(i * 0.7))
            weights.append(w)
        
        return (weights[0] * poly_term + 
                weights[1] * trig_term + 
                weights[2] * radial_term + 
                weights[3] * interaction_term + 
                weights[4] * noise_term)