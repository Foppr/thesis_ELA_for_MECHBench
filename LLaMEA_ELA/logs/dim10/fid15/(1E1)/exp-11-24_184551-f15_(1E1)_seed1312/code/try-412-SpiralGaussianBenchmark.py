import numpy as np

class SpiralGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_peaks = 8
        self.peaks = []
        
        # Create spiral pattern of peaks
        angles = np.linspace(0, 2*np.pi, self.num_peaks, endpoint=False)
        radii = np.logspace(0, 1, self.num_peaks, base=np.e) - 1.0
        for i in range(self.num_peaks):
            x = radii[i] * np.cos(angles[i])
            y = radii[i] * np.sin(angles[i])
            self.peaks.append([x, y])
        
        # Add central peak
        self.peaks.append([0.0, 0.0])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.05
        
        # Multimodal terms - Gaussian peaks in spiral pattern
        multimodal_term = 0.0
        for i in range(len(self.peaks)):
            peak = self.peaks[i]
            if len(peak) != min(2, self.dim):
                continue
                
            # Calculate distance in first two dimensions
            distance_sq = 0.0
            for j in range(min(2, self.dim)):
                distance_sq += (x[j] - peak[j])**2
            
            # Add Gaussian contribution from this peak
            multimodal_term += np.exp(-distance_sq / 2.0) * (1.0 + i * 0.1)
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.sin(x) * 0.02)
        
        return basin_term - multimodal_term + noise