import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic quaternion-inspired harmonic component
        quat = 0.0
        for i in range(self.dim):
            quat += (np.sin(x[i]) * np.cos(x[i]) * np.tan(x[i])) ** 2 + 0.1 * x[i] ** 4
        
        # Dynamic hyperbolic tangent peaks with variable amplitudes
        tanh_peaks = 0.0
        for i in range(self.dim):
            amplitude = 1.0 + 0.5 * np.sin(3 * x[i])
            tanh_peaks += amplitude * np.tanh(2 * x[i]) ** 2
        
        # Adaptive fractal landscape with exponential scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.exp(-np.abs(x[i])) * np.sin(2 ** (i+1) * x[i])
        
        # Multi-scale Gaussian peaks with time-varying centers and widths
        gaussian = 0.0
        scales = [1.0, 0.5, 2.0, 0.25]
        for i in range(self.dim):
            for scale in scales:
                center = scale * np.sin(x[i] ** 2)
                width = 0.3 + 0.7 * np.cos(x[i] ** 2)
                gaussian += np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2))
        
        # Neural-network-like cross-dimensional coupling with sigmoidal interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 1.0 / (1.0 + np.exp(-(x[i] + x[j])))
                cross += coupling * (x[i] ** 2 + x[j] ** 2)
        
        # Resonance peaks with complex logarithmic and trigonometric mixing
        resonance = 0.0
        for i in range(self.dim):
            resonance += np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.log(np.abs(x[i]) + 2) * np.tan(x[i] / 2)
        
        # Asymmetric gradient deception with polynomial-trigonometric hybrid mixing
        deception = 0.0
        for i in range(self.dim):
            deception += (x[i] ** 5 - 3 * x[i] ** 3 + 2 * x[i]) * np.sin(x[i] ** 2)
        
        # Complex cross-dimensional interactions with dynamic scaling factors
        complex_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                scale_factor = 1.0 + 0.3 * np.sin(x[i] * x[j])
                complex_cross += scale_factor * np.exp(-0.5 * ((x[i] - x[j]) ** 2)) * (x[i] ** 3 + x[j] ** 3)
        
        # Combine all components with varying weights
        return 0.15 * quat + 0.2 * tanh_peaks + 0.15 * fractal + 0.25 * gaussian + 0.1 * cross + 0.05 * resonance + 0.05 * deception + 0.05 * complex_cross