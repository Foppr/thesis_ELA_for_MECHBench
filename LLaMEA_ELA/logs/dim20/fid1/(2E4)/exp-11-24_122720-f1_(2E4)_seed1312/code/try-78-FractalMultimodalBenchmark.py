import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different dimensions
        self.fractal_params = []
        for i in range(dim):
            self.fractal_params.append({
                'frequency': 2.0 + 0.5 * np.sin(i * np.pi / (dim + 1)),
                'amplitude': 1.0 + 0.3 * np.cos(i * np.pi / (dim + 2)),
                'phase': 0.5 * np.sin(i * np.pi / (dim + 3)),
                'roughness': 0.7 + 0.3 * np.cos(i * np.pi / (dim + 4))
            })
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal component with hierarchical structure
        for i in range(self.dim):
            params = self.fractal_params[i]
            # Base fractal term with varying frequency and amplitude
            fractal_term = params['amplitude'] * np.sin(params['frequency'] * x[i] + params['phase'])
            
            # Add higher-order harmonics for fractal complexity
            for n in range(2, 5):
                fractal_term += (params['amplitude'] / n) * np.sin(n * params['frequency'] * x[i] + params['phase'])
            
            # Apply roughness parameter to create self-similar structure
            roughness_factor = 1.0 + params['roughness'] * np.sin(x[i] * 0.5)
            fractal_term *= roughness_factor
            
            result += fractal_term
        
        # Add multimodal components with adaptive gradient fields
        multimodal_component = 0.0
        for i in range(self.dim):
            # Adaptive gradient field based on dimension index
            grad_field = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            
            # Multimodal terms with varying positions and heights
            modal_term = 0.0
            for j in range(3):
                center = -3.0 + 2.0 * j
                height = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 2) + j)
                width = 0.8 + 0.2 * np.sin(i * np.pi / (self.dim + 3) + j)
                
                # Gaussian-like modal function
                modal_term += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
            multimodal_component += grad_field * modal_term
        
        # Combine components with dimension-dependent weights
        weight1 = 0.4 + 0.1 * np.sin(self.dim * np.pi / 8)
        weight2 = 0.6 + 0.1 * np.cos(self.dim * np.pi / 9)
        
        # Add noise component for additional complexity
        noise = 0.05 * np.sum(np.random.randn(self.dim) * x)
        
        return weight1 * result + weight2 * multimodal_component + noise