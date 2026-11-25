import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-inspired chaotic oscillation component
        quaternion = 0.0
        for i in range(self.dim):
            quaternion += (np.sin(x[i]) * np.cos(x[i])) ** 2 + 0.1 * x[i] ** 4
        
        # Dynamic hyperbolic tangent peaks with adaptive scaling
        tanh_peaks = 0.0
        for i in range(self.dim):
            tanh_peaks += np.tanh(3 * x[i]) ** 2 + 0.5 * np.tanh(x[i]) * np.sin(2 * x[i])
        
        # Adaptive fractal coupling with cross-dimensional polynomial interactions
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                fractal_coupling += (x[i] ** 2 + x[j] ** 2) * np.sin(5 * (x[i] - x[j])) * np.cos(5 * (x[i] + x[j]))
        
        # Multi-scale Gaussian distributions with time-varying skewness and kurtosis
        gaussian = 0.0
        scales = [1.0, 0.5, 2.0]
        for i in range(self.dim):
            for scale in scales:
                center = scale * np.sin(x[i])
                width = 0.5 + 0.5 * np.cos(x[i])
                amplitude = 1.0 + 0.3 * np.sin(3 * x[i])
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2))
        
        # Cross-dimensional polynomial couplings with dynamic weights
        cross_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 1.0 + 0.2 * np.sin(x[i] + x[j])
                cross_poly += weight * (x[i] ** 3 + x[j] ** 3) * np.exp(-0.1 * ((x[i] - x[j]) ** 2))
        
        # Neural-network-like adaptive coupling with sigmoidal activation
        neural_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                activation = 1 / (1 + np.exp(-x[i] - x[j]))
                neural_coupling += activation * np.sin(2 * (x[i] - x[j])) * (x[i] ** 2 + x[j] ** 2)
        
        # Enhanced gradient deception through modified polynomial-trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            poly_term = x[i] ** 5 - 2 * x[i] ** 3 + x[i]
            trig_term = np.sin(2 * x[i]) + 0.5 * np.cos(3 * x[i])
            deception += poly_term * trig_term * (1 + 0.2 * np.sin(x[i]))
        
        # Combine all components with adjusted weights for improved algorithm discrimination
        return 0.25 * quaternion + 0.20 * tanh_peaks + 0.15 * fractal_coupling + 0.15 * gaussian + 0.15 * cross_poly + 0.08 * neural_coupling + 0.02 * deception