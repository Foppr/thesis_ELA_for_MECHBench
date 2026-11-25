import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_scaled**2)
        
        # Fractal-like component with logarithmic spiral patterns
        fractal = 0.0
        for i in range(self.dim):
            r = np.sqrt(x_scaled[i]**2 + 0.01)
            theta = np.arctan2(x_scaled[i], 0.1)
            # Logarithmic spiral pattern with multiple frequencies
            spiral = np.sin(5.0 * theta + 2.0 * np.log(r + 1.0)) * np.cos(3.0 * theta - 1.5 * np.log(r + 1.0))
            fractal += spiral * np.exp(-r**2)
        
        # Multi-scale harmonic interactions with varying amplitudes
        harmonics = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(10.0 * x_scaled[i])
            freq = 8.0 + 4.0 * np.cos(5.0 * x_scaled[i])
            phase = 2.0 * np.sin(3.0 * x_scaled[i])
            harmonics += amp * np.sin(freq * x_scaled[i] + phase) * np.cos(2.0 * x_scaled[i]**2)
        
        # Cross-dimensional coupling with fractal-like interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                # Fractal distance coupling with exponential decay
                coupling = np.sin(15.0 * dist) * np.cos(7.0 * dist) * np.exp(-dist**4)
                cross_coupling += coupling
        
        # Peak formation with self-similar structure
        peaks = 0.0
        for i in range(self.dim):
            # Multiple peaks with varying heights and widths
            peak1 = 2.0 * np.exp(-((x_scaled[i] - 0.5)**2 + (x_scaled[i] + 0.3)**2) / 0.2)
            peak2 = 1.5 * np.exp(-((x_scaled[i] + 0.7)**2 + (x_scaled[i] - 0.2)**2) / 0.15)
            peaks += peak1 + peak2
        
        # Combine all components with dynamic weighting
        result = quadratic + 0.8 * fractal + 0.6 * harmonics + 0.4 * cross_coupling + 0.7 * peaks
        
        # Add fractal noise for increased complexity
        noise = 0.02 * np.random.uniform(-1.0, 1.0) * (1.0 + 0.3 * np.sin(20.0 * np.sum(x_scaled**2)))
        result += noise
        
        return result