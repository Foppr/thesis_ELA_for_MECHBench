import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulation component
        chaotic_modulation = 0.0
        for i in range(self.dim):
            chaotic_modulation += np.sin(13 * x[i]) * np.cos(7 * x[i]) + 0.3 * np.sin(29 * x[i])
        
        # Dynamic multi-peak Gaussian distributions with time-varying skewness
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(1, 4):
                center = j * np.sin(x[i] / j)
                width = 0.5 + 0.5 * np.cos(x[i] / j)
                amplitude = 1.0 + 0.2 * np.sin(5 * x[i])
                skewness = 0.3 * np.sin(2 * x[i])
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2)) * (1 + skewness * (x[i] - center))
        
        # Fractal-like recursive saddle structures
        saddle = 0.0
        for i in range(self.dim):
            saddle += (np.sin(x[i]) ** 2 - np.cos(x[i]) ** 2) * np.exp(-0.1 * x[i] ** 2)
        
        # Cross-dimensional polynomial couplings with adaptive weights
        cross_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 1.0 + 0.5 * np.sin(x[i] * x[j])
                cross_poly += weight * (x[i] ** 2 + x[j] ** 2) * np.cos(3 * (x[i] - x[j]))
        
        # Adaptive neural-network-like coupling with tanh activation
        neural_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                activation = np.tanh(x[i] + x[j])
                neural_coupling += activation * np.sin(2 * (x[i] - x[j])) * (x[i] ** 2 + x[j] ** 2)
        
        # Gradient deception through polynomial-trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            poly_term = x[i] ** 4 - 2 * x[i] ** 2 + 0.5
            trig_term = np.sin(3 * x[i]) + 0.5 * np.cos(5 * x[i])
            deception += poly_term * trig_term * (1 + 0.3 * np.sin(x[i]))
        
        # Combine all components with adjusted weights for improved algorithm discrimination
        return 0.25 * chaotic_modulation + 0.20 * gaussian_peaks + 0.15 * saddle + 0.15 * cross_poly + 0.15 * neural_coupling + 0.10 * deception