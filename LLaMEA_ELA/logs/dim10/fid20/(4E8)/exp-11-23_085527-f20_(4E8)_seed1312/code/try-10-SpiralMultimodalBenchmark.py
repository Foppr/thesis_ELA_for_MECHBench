import numpy as np

class SpiralMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_minima = 8
        self.angle_step = 2 * np.pi / self.num_minima
        self.radius_decay = 0.8
        self.global_minima = []
        # Generate spiral pattern of global minima
        for i in range(self.num_minima):
            angle = i * self.angle_step
            radius = self.radius_decay ** i
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            self.global_minima.append([x, y])
        # Pad with zeros for higher dimensions
        while len(self.global_minima[0]) < dim:
            for i in range(len(self.global_minima)):
                self.global_minima[i].append(0.0)
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term
        basin = 0.1 * np.sum(x**2)
        
        # Spiral multimodal term
        multimodal = 0
        for i in range(len(self.global_minima)):
            center = np.array(self.global_minima[i][:self.dim])
            distance = np.sum((x - center)**2)
            # Add exponentially decaying contribution for each minimum
            weight = np.exp(-i * 0.5) * (1.0 + 0.3 * np.sin(i))
            multimodal += weight * np.exp(-distance / 1.0)
        
        return basin - multimodal