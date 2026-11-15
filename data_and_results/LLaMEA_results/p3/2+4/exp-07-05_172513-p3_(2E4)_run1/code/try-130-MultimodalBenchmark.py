import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Global spiral basin term for attraction to center
        spiral = np.sum((x_scaled**2 + 0.1 * np.sin(10 * np.pi * x_scaled))**0.5)
        
        # Multiple Gaussian peaks with varying heights and widths
        peaks = 0
        for i in range(5):
            peak_x = np.sin(i * np.pi / 5) * 0.5
            peak_y = np.cos(i * np.pi / 5) * 0.5
            peaks += 3.0 * np.exp(-5.0 * ((x_scaled - peak_x)**2 + (x_scaled - peak_y)**2))
        
        # Sinusoidal modulation for increased ruggedness
        modulation = np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled))
        
        # Cross-dimensional coupling with interaction terms
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x_scaled[i] * x_scaled[i+1] * np.sin(5 * np.pi * (x_scaled[i] + x_scaled[i+1])))
        
        # Additional high-frequency noise component
        noise = np.sum(0.5 * np.sin(30 * np.pi * x_scaled) * np.cos(25 * np.pi * x_scaled))
        
        # Combined function with adjusted weights
        return 0.5 * spiral + 2.0 * peaks + 1.5 * modulation + 0.3 * coupling + 0.2 * noise