import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial term with varying degrees and adaptive coefficients
        poly_term = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)
            coeff = 1.0 / (1.0 + 0.15 * i)
            poly_term += coeff * (x_normalized[i] ** degree)
        
        # Trigonometric component with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (1 + 0.6 * np.sin(i * 0.4))
            amp = 1.0 + 0.4 * np.cos(i * 0.5)
            trig_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.8)
        
        # Radial basis function component with adaptive width
        radial_term = 0.0
        for i in range(self.dim):
            width = 0.6 + 0.3 * np.sin(i * 0.7)
            radial_term += np.exp(-0.5 * (x_normalized[i] / width) ** 2)
        
        # Cross-dimensional interaction with coupling strength
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + 0.3 * np.abs(x_normalized[i] - x_normalized[j]))
                interaction_term += coupling * (x_normalized[i] ** 2 + x_normalized[j] ** 2)
        
        # Chaotic phase coupling term
        chaotic_term = 0.0
        for i in range(self.dim):
            phase = np.sin(x_normalized[i] * np.pi * 2) * np.cos(x_normalized[i] * np.pi * 1.5)
            chaotic_term += phase * (1.0 + 0.2 * np.sin(i * 0.3))
        
        # Fractal-like curvature interaction
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(x_normalized[i] ** 3) * np.cos(x_normalized[i] ** 2) * (1.0 + 0.15 * i)
        
        # Quantum-inspired interference term
        quantum_term = 0.0
        for i in range(self.dim):
            quantum_term += np.sin(x_normalized[i] * np.pi * 3) * np.cos(x_normalized[i] * np.pi * 2.5) * (1.0 - 0.1 * i)
        
        # Combine all terms with optimized weights
        return (0.25 * poly_term + 
                0.2 * trig_term + 
                0.15 * radial_term + 
                0.15 * interaction_term + 
                0.1 * chaotic_term + 
                0.08 * fractal_term + 
                0.07 * quantum_term)