import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with dynamic exponents
        poly_chaos = 0
        for i in range(self.dim):
            exp_factor = 2 + 0.5 * np.sin(0.3 * i)
            poly_chaos += (x[i]**exp_factor) * (1 + 0.2 * np.cos(i))
        
        # Periodic wave interference component
        wave_interference = 0
        for i in range(self.dim):
            freq1 = 1.0 + 0.3 * np.sin(0.2 * i)
            freq2 = 1.5 + 0.4 * np.cos(0.2 * i)
            wave_interference += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * 
                                np.exp(-0.1 * x[i]**2))
        
        # Probabilistic basin attraction component
        basin_attraction = 0
        for i in range(self.dim):
            # Randomly selected attractor locations
            attractor = 3.0 * np.sin(0.5 * i)
            prob = 0.5 + 0.3 * np.cos(0.4 * i)
            basin_attraction += prob * (x[i] - attractor)**2 * np.exp(-0.2 * (x[i] - attractor)**2)
        
        # Dynamic conditioning component
        conditioning = 0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.8 * np.sin(0.3 * i)
            conditioning += x[i]**2 * cond_factor
        
        # Cross-dimensional coupling with adaptive weights
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.7 + 0.3 * np.sin(0.2 * (i + j))
                coupling += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric oscillation component
        asymmetric_osc = 0
        for i in range(self.dim):
            asym_factor = 1.2 + 0.4 * np.sin(0.5 * i)
            asymmetric_osc += (np.sin(asym_factor * x[i]) * np.exp(-0.1 * x[i]**2) +
                              np.cos(asym_factor * x[i]) * np.exp(-0.15 * x[i]**2))
        
        # Multi-modal peak structure with varying heights and widths
        multimodal = 0
        peak_locations = [2.0, -2.0, 1.0, -1.0]
        for i in range(self.dim):
            peak_idx = i % len(peak_locations)
            loc = peak_locations[peak_idx]
            height = 1.5 + 0.5 * np.sin(0.3 * i)
            width = 0.8 + 0.2 * np.cos(0.2 * i)
            multimodal += height * np.exp(-0.5 * ((x[i] - loc) / width)**2)
        
        # Combine all components with optimized weights
        return (poly_chaos * 0.3 +
                wave_interference * 0.4 +
                basin_attraction * 0.25 +
                conditioning * 0.3 +
                coupling * 0.35 +
                asymmetric_osc * 0.2 +
                multimodal * 0.4)