import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with mixed monomials
        poly_chaos = np.sum(x_norm**2 + 0.5 * x_norm**3 + 0.3 * x_norm**4 + 0.1 * x_norm**5)
        
        # Radial basis functions with varying widths and centers
        rbf = 0.0
        centers = np.linspace(-0.8, 0.8, 5)
        widths = np.linspace(2.0, 8.0, 5)
        for i, (c, w) in enumerate(zip(centers, widths)):
            rbf += np.exp(-w * (x_norm - c)**2)
        
        # Sine-cosine coupling terms with varying frequencies
        coupling = 0.0
        frequencies = [5, 10, 15, 20]
        for i in range(len(frequencies)):
            freq = frequencies[i]
            coupling += np.sin(freq * x_norm) * np.cos(freq * x_norm)
        
        # Cross-dimensional polynomial interactions
        cross_poly = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_poly += (x_norm[i]**2 * x_norm[i+1] + 
                              x_norm[i] * x_norm[i+1]**2 + 
                              0.5 * x_norm[i]**3 * x_norm[i+1]**3)
        
        # Chaotic sine-cosine component with dynamic coupling
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(20 * x_norm[i] * x_norm[i+1]) * np.cos(15 * x_norm[i] * x_norm[i+1]) + \
                          0.3 * np.sin(25 * x_norm[i]**2 * x_norm[i+1]**2) * np.cos(20 * x_norm[i]**2 * x_norm[i+1]**2)
        
        # Asymmetric exponential and polynomial mixture
        asym_exp = np.sum(np.exp(-x_norm**2) * np.abs(x_norm) + 0.5 * np.exp(-2 * x_norm**2) * x_norm**3)
        
        # High-frequency trigonometric component
        high_freq = np.sum(np.sin(50 * x_norm) + 0.5 * np.cos(60 * x_norm) + 0.3 * np.sin(70 * x_norm))
        
        # Additional multimodal term with multiple local minima
        multimodal = 0.0
        for i in range(1, 6):
            multimodal += np.exp(-((x_norm - i*0.2)**2 + (x_norm + i*0.2)**2) / 0.1) + \
                         0.5 * np.exp(-((x_norm - i*0.3)**2 + (x_norm + i*0.3)**2) / 0.05)
        
        # Combine all components with appropriate weights
        result = (0.25 * poly_chaos + 
                  0.2 * rbf + 
                  0.15 * coupling + 
                  0.1 * cross_poly + 
                  0.1 * chaotic + 
                  0.08 * asym_exp + 
                  0.07 * high_freq + 
                  0.05 * multimodal)
        
        # Add small noise for non-triviality
        noise = 0.001 * np.random.random()
        
        return result + noise