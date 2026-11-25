import numpy as np

class ChaoticGaussianPeakBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for different dimensions
        self.scaling_factors = [1.0 + 0.1 * i for i in range(100)]
    
    def f(self, x):
        x = np.array(x)
        
        # Dynamic Gaussian peak landscape with chaotic modulation
        result = 0.0
        num_peaks = max(3, self.dim // 2)
        
        for i in range(num_peaks):
            # Chaotic position adjustment using sine and cosine modulations
            peak_x = 2.5 * np.sin(i * 1.7) + 1.5 * np.cos(i * 0.9)
            peak_y = 2.5 * np.cos(i * 1.3) + 1.5 * np.sin(i * 0.7)
            
            # Adaptive peak height based on dimension
            peak_height = 10.0 * (1.0 + 0.3 * np.sin(i * 0.5))
            
            # Distance from peak with dynamic scaling
            dist_x = x[0] - peak_x if self.dim > 0 else 0.0
            dist_y = x[1] - peak_y if self.dim > 1 else 0.0
            
            # Multi-dimensional distance calculation with chaotic weights
            dist_sq = dist_x**2 + dist_y**2
            for j in range(2, min(self.dim, 5)):
                dist_sq += (x[j] - (peak_x * np.sin(j * 0.3) + peak_y * np.cos(j * 0.4)))**2
            
            # Gaussian peak with chaotic amplitude and width
            amplitude = peak_height * (1.0 + 0.2 * np.sin(i * 1.1))
            width = 1.0 + 0.5 * np.cos(i * 0.8)
            
            result += amplitude * np.exp(-dist_sq / (2.0 * width**2))
        
        # Cross-dimensional chaotic coupling with varying strengths
        coupling_strength = 0.5 + 0.3 * np.sin(self.dim * 0.4)
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.sin(x[i] * x[j]) * coupling_strength
                result += 0.2 * coupling
        
        # Adaptive penalty regions with dynamic boundaries
        penalty = 0.0
        for i in range(self.dim):
            # Dynamic boundary based on dimension and position
            boundary = 3.0 + 1.5 * np.sin(i * 0.6)
            if abs(x[i]) > boundary:
                penalty += (abs(x[i]) - boundary)**2 * (1.0 + 0.1 * i)
        
        # Fractal-like conditioning with dimension-dependent scaling
        conditioning = 1.0 + 0.2 * np.sin(self.dim * 0.3) + 0.1 * np.cos(self.dim * 0.7)
        
        # Final landscape combination with chaotic weight adjustment
        total = result * conditioning + penalty
        
        # Apply global scaling factor based on dimension
        if self.dim < len(self.scaling_factors):
            total *= self.scaling_factors[self.dim]
        else:
            total *= (1.0 + 0.1 * self.dim)
            
        return total