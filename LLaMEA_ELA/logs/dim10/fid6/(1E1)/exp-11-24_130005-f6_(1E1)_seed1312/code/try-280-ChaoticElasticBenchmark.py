import numpy as np

class ChaoticElasticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Hyper-elastic strain energy component with polynomial potentials
        elastic_energy = 0.0
        for i in range(self.dim):
            # Non-linear elastic response with multiple stiffness regions
            xi = x_scaled[i]
            elastic_energy += (xi**2 + 0.3 * xi**4 + 0.1 * xi**6) * (1.0 + 0.2 * np.sin(5.0 * xi))
        
        # Chaotic interaction terms with exponential coupling
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited long-range interactions
                # Exponentially decaying chaotic coupling
                coupling = np.exp(-2.0 * (i - j)**2) * np.sin(3.0 * x_scaled[i] * x_scaled[j])
                chaotic_interaction += coupling
        
        # Multi-modal peak landscape with saddle points and local minima
        multimodal = 0.0
        for i in range(self.dim):
            # Multiple Gaussian peaks with varying heights and widths
            peak_heights = [1.5, 2.0, 1.0, 1.8]
            peak_positions = [-0.7, 0.0, 0.7, -0.3]
            widths = [0.4, 0.6, 0.5, 0.3]
            
            for h, p, w in zip(peak_heights, peak_positions, widths):
                multimodal -= h * np.exp(-0.5 * ((x_scaled[i] - p) / w)**2)
        
        # Dimensionally scaled harmonic oscillators with varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.8)
            amplitude = 1.0 + 0.3 * np.cos(i * 0.6)
            harmonic += amplitude * (freq * x_scaled[i])**2
        
        # Saddle point structure with mixed quadratic terms
        saddle = 0.0
        for i in range(self.dim):
            # Alternating signs for saddle point creation
            sign = (-1)**i
            saddle += sign * x_scaled[i]**2 * (x_scaled[i] - 0.5)**2
        
        # Combined landscape with adaptive weights
        return 1.2 * elastic_energy + 0.8 * chaotic_interaction + 1.0 * multimodal + 0.6 * harmonic + 0.4 * saddle