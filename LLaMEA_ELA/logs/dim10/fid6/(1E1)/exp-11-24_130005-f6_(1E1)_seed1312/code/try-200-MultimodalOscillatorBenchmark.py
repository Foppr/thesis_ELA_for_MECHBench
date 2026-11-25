import numpy as np

class MultimodalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Oscillatory component with multiple frequencies and amplitudes
        oscillation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.4 * np.cos(i * 0.7)
            oscillation += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.3)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        num_centers = min(5, self.dim)
        for c in range(num_centers):
            center = np.sin(c * 0.5) * 0.8
            width = 0.5 + 0.3 * np.cos(c * 0.4)
            rbf += np.exp(-width * (x_scaled - center)**2).sum()
        
        # Cross-dimensional coupling with interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling strength and interaction type
                coupling += 0.3 * np.sin(x_scaled[i] * x_scaled[j]) * \
                           np.cos(0.5 * (x_scaled[i] + x_scaled[j]))
        
        # Periodic landscape with varying periods across dimensions
        periodic = 0.0
        for i in range(self.dim):
            period = 2.0 + 0.8 * np.sin(i * 0.6)
            periodic += np.sin(period * x_scaled[i]) * np.cos(period * x_scaled[i] * 0.4)
        
        # Asymmetric landscape with different behavior in positive and negative regions
        asymmetry = 0.0
        for i in range(self.dim):
            if x_scaled[i] >= 0:
                asymmetry += 0.2 * np.sin(3.0 * x_scaled[i]) * np.exp(-x_scaled[i]**2)
            else:
                asymmetry += 0.2 * np.cos(2.0 * x_scaled[i]) * np.exp(-x_scaled[i]**2)
        
        # Combine all components with modified weights
        return 0.8 * oscillation + 1.2 * rbf + 0.6 * coupling + 0.4 * periodic + 0.3 * asymmetry